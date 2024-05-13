from django.contrib import messages
from django.db.models import (
    Q,
    IntegerField,
)
from django.db.models.expressions import RawSQL

from index import check
from utils.constants import (
    EXPERIENCE_CHOICES,
    EMPLOYMENT_CHOICES,
    SCHEDULE_CHOICES,
)
from index.models import (
    Vacancy,
    Company,
    Header,
    VacancyResponse,
)


def get_context_data(request):
    header = get_header(
        request=request,
    )
    companies = get_companies(
        request=request,
    )
    vacancies = get_vacancies(
        request=request,
    )
    return {
        'header': header,
        'EXPERIENCE_CHOICES': EXPERIENCE_CHOICES,
        'EMPLOYMENT_CHOICES': EMPLOYMENT_CHOICES,
        'SCHEDULE_CHOICES': SCHEDULE_CHOICES,
        'vacancies': vacancies,
        'companies': companies,
    }


def get_header(request):
    try:
        header = Header.objects.filter().first()
    except Exception as exc:
        print(f'Возникла ошибка при загрузке шапки: {exc}')
        messages.warning(
            request=request,
            message='Не получилось загрузить шапку сайта'
        )
        header = None
    return header


def get_vacancies(request):
    try:
        vacancies = Vacancy.objects.filter(
            company__hidden=False,
            hidden=False
        )
    except Exception as exc:
        print(f'Возникла ошибка при загрузке вакансий: {exc}')
        messages.warning(
            request=request,
            message='Не получилось загрузить вакансии'
        )
        vacancies = None
    return vacancies


def get_companies(request):
    try:
        companies = Company.objects.filter(hidden=False)
    except Exception as exc:
        print(f'Возникла ошибка при загрузке компаний: {exc}')
        messages.warning(
            request=request,
            message='Не получилось загрузить компании'
        )
        companies = None
    return companies


def get_vacancy(request, pk) -> (int, Vacancy):
    try:
        vacancy = Vacancy.objects.filter(pk=pk).first()
    except Exception as exc:
        print(f'Возникла ошибка при поиске вакансии {exc}')
        messages.error(
            request=request,
            message='Возникла ошибка при поиске вакансии',
        )
        return 500, None
    return 200, vacancy


def send_response(request, vacancy):
    if not check.response_data(request=request):
        return 400
    data = request.POST
    files = request.FILES
    try:
        VacancyResponse.objects.create(
            vacancy=vacancy,
            email=data['email'],
            resume=files['resume'],
            covering_letter=data.get('covering_letter'),
        )
    except Exception as exc:
        print(f'Возникла ошибка при отправке отклика {exc}')
        messages.error(
            request=request,
            message='Возникла ошибка при отправке отклика',
        )
        return 500
    messages.success(
        request=request,
        message='Ваш отклик успешно отправлен',
    )
    return 200


def filter_vacancies(request, vacancies):
    data = request.GET
    filters = get_filters(
        data=data,
    )
    vacancies = vacancies.annotate(
        salary_number=RawSQL(
            "COALESCE(NULLIF(REGEXP_REPLACE(salary, '\D','','g'), '')::numeric, 0)",
            params=[],
            output_field=IntegerField()
        )
    )
    salary = int(data['salary'].replace(' ', '')) if data['salary'] else 0
    try:
        vacancies = vacancies.filter(
            Q(company__name__icontains=data['search']) | Q(title__icontains=data['search']),
            **filters,
            salary_number__gte=salary,
        )
    except Exception as exc:
        print(f'Возникла ошибка при фильтрации {exc}')
    return vacancies


def get_filters(data):
    keys = [
        'company',
        'experience',
        'employment',
        'schedule',
    ]
    filters = {}
    for key in keys:
        if data[key] != '':
            filters[key] = data[key]
    return filters
