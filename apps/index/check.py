import os.path

from django.contrib import messages
from django.core.exceptions import ValidationError
from django.core.validators import validate_email


def required_data(request):
    data = request.POST
    keys = [
        ('email', 'адрес электронной почты'),
    ]
    for key, field_name in keys:
        if data.get(key) is None:
            messages.error(
                request=request,
                message=f'Поле {field_name} обязательно для заполнения'
            )
            return False
        return True


def required_files(request):
    files = request.FILES
    keys = [
        ('resume', 'резюме'),
    ]
    for key, field_name in keys:
        if files.get(key) is None:
            messages.error(
                request=request,
                message=f'Файл {field_name} обязателен для загрузки'
            )
            return False
        return True


def is_email_valid(request):
    email = request.POST.get('email')
    try:
        validate_email(email)
    except ValidationError as exc:
        print(f'Адрес электронной почты не валиден {exc}')
        messages.error(
            request=request,
            message='Адрес электронной почты некорректный',
        )
        return False
    return True


def is_resume_valid(request):
    resume = request.FILES['resume']
    extension = os.path.splitext(resume.name)[1]
    valid_extensions = ['.doc', '.docx', '.pdf']
    if extension not in valid_extensions:
        messages.error(
            request=request,
            message='Недопустимый тип файла резюме',
        )
        return False
    return True


def response_data(request):
    if not required_data(request=request) or not required_files(request=request):
        return False
    if not is_email_valid(request=request) or not is_resume_valid(request=request):
        return False
    return True
