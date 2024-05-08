from django.shortcuts import render
from django.views import View

from headers.models import Header
from vacancies.models import (
    Vacancy,
    Company,
)


class IndexView(View):
    def get(self, request, *args, **kwargs):
        header = Header.objects.first()
        experience = Vacancy.EXPERIENCE_CHOICES
        employment = Vacancy.EMPLOYMENT_CHOICES
        schedule = Vacancy.SCHEDULE_CHOICES
        vacancies = Vacancy.objects.filter(company__hidden=False, hidden=False)
        companies = Company.objects.filter(hidden=False)
        context = {
            'header': header,
            'EXPERIENCE_CHOICES': experience,
            'EMPLOYMENT_CHOICES': employment,
            'SCHEDULE_CHOICES': schedule,
            'vacancies': vacancies,
            'companies': companies,
        }
        return render(
            request=request,
            template_name='index.html',
            context=context,
        )
