"""Admin for django-error-report-2 package."""
from __future__ import absolute_import, unicode_literals

from django.contrib import admin
from django.utils.decorators import method_decorator
from django.views.decorators.clickjacking import xframe_options_sameorigin
from django.views.decorators.csrf import csrf_protect

from error_report.models import Error

csrf_protect_m = method_decorator(csrf_protect)


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

    @csrf_protect_m
    @xframe_options_sameorigin
    def changeform_view(self, request, object_id=None, form_url='', extra_context=None):
        """Adding xref to the changeform view"""
        return super().changeform_view(request, object_id, form_url, extra_context=extra_context)

    @xframe_options_sameorigin
    def add_view(self, request, form_url='', extra_context=None):
        """Adding xref to the add view"""
        return super().add_view(request, form_url, extra_context=extra_context)

    @xframe_options_sameorigin
    def change_view(self, request, object_id, form_url='', extra_context=None):
        """Adding xref to the change view"""
        return super().change_view(request, object_id, form_url, extra_context=extra_context)

    @csrf_protect_m
    @xframe_options_sameorigin
    def changelist_view(self, request, extra_context=None):
        """Adding xref to the changelist view"""
        return super().changelist_view(request, extra_context=extra_context)

    @csrf_protect_m
    @xframe_options_sameorigin
    def delete_view(self, request, object_id, extra_context=None):
        """Adding xref to the delete view"""
        return super().delete_view(request, object_id, extra_context=extra_context)


admin.site.register(Error, ErrorAdmin)
