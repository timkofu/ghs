
from django.contrib import admin
from django.contrib.admin import site
#from django.db.transaction import atomic
from django.db import IntegrityError
from django.db.models.base import ObjectDoesNotExist
from django.conf import settings

from github import Github

from .models import Project, Language

from .operations import Ops



# Disable delete action sitewide
site.disable_action('delete_selected')

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
    actions = ('fetch', 'update', 'delete')

    #@atomic
    def fetch(self, request, queryset):

        my_stars = self.my_github_handle.get_user(settings.GH_USERNAME).get_starred()
        saved_stars = Project.objects.all()
        ops = Ops(my_stars, saved_stars)

        # Add
        ops.add_stars({'language':Language, 'project':Project}, expected_exceptions=IntegrityError)
        
        self.message_user(request, "Fetched")
    fetch.short_description = 'Fetch'


    def update(self, request, queryset):

        my_stars = self.my_github_handle.get_user(settings.GH_USERNAME).get_starred()
        saved_stars = Project.objects.all()
        ops = Ops(my_stars, saved_stars)

        # Update
        ops.update_metadata(expected_exceptions=ObjectDoesNotExist)
        
        self.message_user(request, "Updated")
    update.short_description = 'Update'


    def delete(self, request, queryset):

        my_stars = self.my_github_handle.get_user(settings.GH_USERNAME).get_starred()
        saved_stars = Project.objects.all()
        ops = Ops(my_stars, saved_stars)

        # Delete
        ops.fallen()
        
        self.message_user(request, "Deleted")
    delete.short_description = 'Delete'


    # Hack, so I dont have to selct records; selects all
    def changelist_view(self, request, extra_context=None):
        if 'action' in request.POST and \
        request.POST['action'] in ['fetch','update','delete']:
            post = request.POST.copy()
            post.update(
                {admin.ACTION_CHECKBOX_NAME: None} # Yep, no selections
            )
            request._set_post(post)
        return super().changelist_view(request, extra_context)

