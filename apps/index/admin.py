from django.contrib import admin
from django.db.models import F

from solo.admin import SingletonModelAdmin

from index.models import (
    Company,
    Vacancy,
    VacancyResponse,
    Header,
)
from index.forms import (
    CompanyAdminForm,
    VacancyAdminForm,
    HeaderFormAdmin,
)


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
    search_fields = [
        'name',
    ]


class VacancyResponseInline(admin.StackedInline):
    model = VacancyResponse
    readonly_fields = [
        'email',
        'resume',
        'covering_letter',
    ]
    ordering = [
        'viewed',
        'created_at',
    ]

    def has_add_permission(self, request, obj):
        return False


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    form = VacancyAdminForm
    list_display = [
        'title',
        'company',
        'hidden',
        'company_hidden',
    ]
    inlines = [
        VacancyResponseInline,
    ]
    list_filter = [
        'company__name',
        'hidden',
    ]
    search_fields = [
        'title',
        'company__name',
    ]
    ordering = [
        'created_at',
    ]

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.annotate(company_hidden=F('company__hidden'))

    def company_hidden(self, instance):
        return instance.company_hidden

    company_hidden.boolean = True
    company_hidden.short_description = 'Компания скрыта'


@admin.register(Header)
class HeaderAdmin(SingletonModelAdmin):
    form = HeaderFormAdmin
    list_display = [
        'title',
    ]
