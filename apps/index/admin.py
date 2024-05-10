from django.contrib import admin

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


@admin.register(Header)
class HeaderAdmin(SingletonModelAdmin):
    form = HeaderFormAdmin
    list_display = [
        'title',
    ]
