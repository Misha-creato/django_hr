from ckeditor.widgets import CKEditorWidget

from django import forms
from django.contrib import admin

from headers.models import Header


class HeaderFormAdmin(forms.ModelForm):
    class Meta:
        model = Header
        fields = '__all__'
        widgets = {
            'description': CKEditorWidget(),
        }


@admin.register(Header)
class HeaderAdmin(admin.ModelAdmin):
    form = HeaderFormAdmin
    list_display = [
        'title',
    ]
