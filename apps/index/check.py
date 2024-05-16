import os.path

from django.core.exceptions import ValidationError
from django.core.validators import validate_email

from utils.constants import RESUME_VALID_EXTENSIONS


def required_data(data) -> bool:
    keys = [
        'email',
    ]
    for key in keys:
        if not data.get(key):
            print(f'Отсутствие ключа {key}')
            return False
    return True


def required_files(files) -> bool:
    keys = [
        'resume',
    ]
    for key in keys:
        if not files.get(key):
            print(f'Отсутствие файла {key}')
            return False
    return True


def is_email_valid(email) -> bool:
    try:
        validate_email(email)
    except ValidationError as exc:
        print(f'Адрес электронной почты не валиден {exc}')
        return False
    return True


def is_file_extension_valid(file, extensions) -> bool:
    file_extension = os.path.splitext(file.name)[1]
    if file_extension not in extensions:
        print(f'Расширение файла {file.name} не валидно')
        return False
    return True


def response_data(data, files) -> bool:
    data_checks = [
        required_data,
    ]
    files_checks = [
        required_files,
    ]
    for data_check, file_check in zip(data_checks, files_checks):
        if not data_check(data):
            return False
        if not file_check(files):
            return False

    if not is_email_valid(data['email']):
        return False
    if not is_file_extension_valid(files['resume'], RESUME_VALID_EXTENSIONS):
        return False

    return True
