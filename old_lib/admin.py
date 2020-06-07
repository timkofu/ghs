
from django.contrib import admin
from django.contrib.admin import site
from django.db.models.base import ObjectDoesNotExist
from django.utils.html import format_html

from .models import Project, Language
from .tasks import mega_update
from .ops import get_ghh



# Disable delete action sitewide
site.disable_action('delete_selected')

@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):

    readonly_fields = ('name', )


@admin.register(Project)
class ProjectsAdmin(admin.ModelAdmin):

    date_hierarchy = 'add_date'
    list_select_related = (
        'language',
    )
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
        return format_html('<a href="{0}" target="_blank">{1}</a>'.format(obj.url, obj.name))
    #github_link.mark_safe = True
    github_link.short_description = 'GitHub Link'

    ordering = ("-current_stars",)

    # Admin Actions
    actions = ['update']

    def update(self, request, queryset):

        mega_update.delay(
            stars=get_ghh().get_starred(),
            savedstars=Project.objects.all(),
            expected_exceptions=ObjectDoesNotExist
        )

        self.message_user(request, 'Updating, check back in a few minutes.')
    update.short_description = 'Update'


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

