"""Admin for django-error-report-2 package."""
from __future__ import absolute_import, unicode_literals

from django.contrib import admin
from django.views.decorators.clickjacking import xframe_options_sameorigin

from error_report.models import Error


@xframe_options_sameorigin
class ErrorAdmin(admin.ModelAdmin):
    """Admin for Error model."""
    list_display = ('path', 'kind', 'info', 'when')
    list_display_links = ('path',)
    ordering = ('-id',)
    search_fields = ('path', 'kind', 'info', 'data')
    readonly_fields = ('path', 'kind', 'info', 'data', 'when', 'html_iframe')
    fieldsets = (
        (None, {
            'fields': ('kind', 'path', 'info', 'when', 'data', 'html_iframe')
        }),
    )

    def has_delete_permission(self, request, obj=None):
        """Disabling the delete permissions."""
        return True

    def has_add_permission(self, request):
        """Disabling the create permissions."""
        return False


admin.site.register(Error, ErrorAdmin)
