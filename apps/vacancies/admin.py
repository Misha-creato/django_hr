from django.contrib import admin
from ckeditor.widgets import CKEditorWidget
from django import forms

from vacancies.models import (
    Company,
)


class CompanyAdminForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = '__all__'
        widgets = {
            'description': CKEditorWidget(),
        }


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    form = CompanyAdminForm
    list_display = [
        'name',
        'hidden',
    ]
    list_filter = [
        'name',
        'hidden',
    ]
