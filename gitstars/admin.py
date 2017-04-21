
from django.contrib import admin
from django.db.transaction import atomic
from django.db import IntegrityError
from django.db.models.base import ObjectDoesNotExist
from django.conf import settings

from github import Github

from .models import Project, Language



@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):

    readonly_fields = ('name', )


@admin.register(Project)
class ProjectsAdmin(admin.ModelAdmin):

    date_hierarchy = 'add_date'
    list_select_related = True
    readonly_fields = (
        'name', 'full_name','description', 'url', 'initial_stars',
        'current_stars', 'language', 'add_date',
    )

    list_filter = ('language',)
    search_fields = ('name', 'description', 'notes')

    # List display fields and functions
    list_display = (
        'name', 'language', 'description', 'initial_stars',
        'current_stars', 'add_date', 'github_link',
    )

    # List display functions
    def github_link(self, obj):
        return '<a href="{0}" target="_blank">{1}</a>'.format(obj.url, obj.name)
    github_link.allow_tags = True
    github_link.short_description = 'GitHub Link'

    ordering = ("-current_stars",)

    my_github_handle = Github(settings.GH_USERNAME, settings.GH_PASSWORD)
    #def current_stars(self, obj):
    #    cstars = self.my_github_handle.get_repo(obj.full_name).stargazers_count
    #    if cstars > obj.initial_stars:
    #        return "{} ++".format(cstars)
    #    else:
    #        return "{} --".format(cstars)
    #current_stars.short_description = 'Stars'

    # Admin Actions
    actions = ('update',)

    @atomic
    def update(self, request, queryset):

        my_stars = self.my_github_handle.get_user(settings.GH_USERNAME).get_starred()
        saved_stars = Project.objects.all()

        # Adding new stars
        for star in my_stars:
            if all([star.name, star.full_name, star.language, star.description,
                star.html_url, star.stargazers_count]):
                try:
                    lang = Language.objects.get_or_create(name=star.language)[0]
                    Project.objects.get_or_create( #update_or_create exists as well :)
                    # should be faster than get_or_create
                    #Project( <-- this breaks the atomic transaction????
                        name=star.name,
                        full_name=star.full_name,
                        description=star.description,
                        url=star.html_url,
                        initial_stars=star.stargazers_count,
                        current_stars=star.stargazers_count,
                        language=lang,
                    )
                except IntegrityError:
                    pass

        # Remove de-starred
        current_stars = {x.full_name for x in my_stars}
        stored_stars = {x.full_name for x in saved_stars}
        fallen_stars = stored_stars.difference(current_stars)
        for fs in fallen_stars:
            saved_stars.get(full_name=fs).delete()

        # Update current star count, and description
        for star in my_stars:
            try:
                saved_star = saved_stars.get(full_name=star.full_name)
                if saved_star:
                    if saved_star.current_stars != star.stargazers_count:
                        saved_star.current_stars = star.stargazers_count
                    elif saved_star.description != star.description:
                        saved_star.description = star.description
                    saved_star.save()
            except ObjectDoesNotExist:
                continue
        #except Exception:
        #    pass
        self.message_user(request, "Refreshed")
    update.short_description = 'Refresh Stars'

    # Hack, so I dont have to selct records; selects all
    def changelist_view(self, request, extra_context=None):
        if 'action' in request.POST and \
        request.POST['action'] == 'update':
            post = request.POST.copy()
            post.update(
                {admin.ACTION_CHECKBOX_NAME: None} # Yep, no selections
            )
            request._set_post(post)
        return super().changelist_view(request, extra_context)
