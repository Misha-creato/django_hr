from django.contrib import admin
from ckeditor.widgets import CKEditorWidget
from django import forms

from vacancies.models import (
    Company,
    Vacancy,
)
from responses.models import VacancyResponse


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


class VacancyAdminForm(forms.ModelForm):
    class Meta:
        model = Vacancy
        fields = '__all__'
        widgets = {
            'description': CKEditorWidget(),
        }

    def __init__(self, *args, **kwargs):
        super(VacancyAdminForm, self).__init__(*args, **kwargs)
        if self.instance:
            self.fields['company'].queryset = Company.objects.filter(hidden=False)


class VacancyResponseInline(admin.StackedInline):
    model = VacancyResponse
    extra = 0
    ordering = [
        'viewed',
        'created_at',
    ]


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    form = VacancyAdminForm
    list_display = [
        'title',
        'company',
        'hidden',
    ]
    inlines = [
        VacancyResponseInline,
    ]
    list_filter = [
        'company__name',
        'hidden',
    ]
    ordering = [
        'created_at',
    ]

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.filter(company__hidden=False)
