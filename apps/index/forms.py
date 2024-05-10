from ckeditor.widgets import CKEditorWidget
from django_ckeditor_5.widgets import CKEditor5Widget

from django import forms

from index.models import (
    Company,
    Vacancy,
    Header,
)


class CompanyAdminForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = '__all__'
        widgets = {
            'description': CKEditor5Widget(
                attrs={"class": "django_ckeditor_5"},
                config_name='extends'
            ),
        }


class VacancyAdminForm(forms.ModelForm):
    form = CompanyAdminForm
    list_display = [
        'name',
        'hidden',
    ]
    list_filter = [
        'name',
        'hidden',
    ]

    class Meta:
        model = Vacancy
        fields = '__all__'
        widgets = {
            'description': CKEditor5Widget(
                attrs={"class": "django_ckeditor_5"},
                config_name='extends'
            ),
        }

    def __init__(self, *args, **kwargs):
        super(VacancyAdminForm, self).__init__(*args, **kwargs)
        if self.instance:
            self.fields['company'].queryset = Company.objects.filter(hidden=False)


class HeaderFormAdmin(forms.ModelForm):
    class Meta:
        model = Header
        fields = '__all__'
        widgets = {
            'description': CKEditor5Widget(
                attrs={"class": "django_ckeditor_5"},
                config_name='extends'
            ),
        }
