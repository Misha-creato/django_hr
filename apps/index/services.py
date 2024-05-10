from index.models import (
    Vacancy,
    Company,
    Header,
)


def get_context_data():
    experience = Vacancy.EXPERIENCE_CHOICES
    employment = Vacancy.EMPLOYMENT_CHOICES
    schedule = Vacancy.SCHEDULE_CHOICES
    header = None
    companies = None
    vacancies = None
    try:
        header = Header.objects.get()
        vacancies = Vacancy.objects.filter(
            company__hidden=False,
            hidden=False
        )
        companies = Company.objects.filter(hidden=False)
    except Exception as exc:
        print(f'Возникла ошибка {exc}')
    return {
            'header': header,
            'EXPERIENCE_CHOICES': experience,
            'EMPLOYMENT_CHOICES': employment,
            'SCHEDULE_CHOICES': schedule,
            'vacancies': vacancies,
            'companies': companies,
    }
