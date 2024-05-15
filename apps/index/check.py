import os.path

from django.core.exceptions import ValidationError
from django.core.validators import validate_email

from utils.constants import RESUME_VALID_EXTENSIONS


# def required_data(data):
#     keys = [
#         'email',
#     ]
#     for key in keys:
#         if not data.get(key):
#             print(f'Отсутствие ключа {key}')
#             return False
#     return True
#

# def required_files(files):
#     keys = [
#         'resume',
#     ]
#     for key in keys:
#         if not files.get(key):
#             print(f'Отсутствие файла {key}')
#             return False
#     return True


def required_data_and_files(data, files):
    keys = [
        ('email', data),
        ('resume', files),
    ]
    for key, source in keys:
        if not source.get(key):
            print(f'Отсутствует {key}')
            return False
    return True


def is_email_valid(email):
    try:
        validate_email(email)
    except ValidationError as exc:
        print(f'Адрес электронной почты не валиден {exc}')
        return False
    return True


def is_file_extension_valid(file, extensions):
    file_extension = os.path.splitext(file.name)[1]
    if file_extension not in extensions:
        print(f'Расширение файла {file.name} не валидно')
        return False
    return True


def response_data(data, files):
    checks = [
        (required_data_and_files,
         {
             'data': data,
             'files': files,
         }
         ),
        (is_email_valid,
         {
             'email': data.get('email'),
         }
         ),
        (is_file_extension_valid,
         {
             'file': files.get('resume'),
             'extensions': RESUME_VALID_EXTENSIONS,
         }
         ),
    ]
    for check, arguments in checks:
        if not check(**arguments):
            return False
    return True
