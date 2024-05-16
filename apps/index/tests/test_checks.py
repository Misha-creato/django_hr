import json
import os.path

from django.test import TestCase

from index.check import (
    required_data,
    required_files,
    is_email_valid,
    is_file_extension_valid,
)


CUR_DIR = os.path.dirname(__file__)


class ChecksTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.path = f'{CUR_DIR}/fixtures/checks'
        cls.files = f'{CUR_DIR}/fixtures/files'

    def test_required_data(self):
        path = f'{self.path}/required_data'

        fixtures = (
            (True, 'valid'),
            (False, 'invalid'),
        )

        for flag, name in fixtures:
            fixture = f'{flag}_{name}'
            with open(f'{path}/{fixture}_request.json') as file:
                data = json.load(file)

            returned_flag = required_data(
                data=data,
            )

            self.assertEqual(returned_flag, flag, msg=fixture)

    def test_required_files(self):
        path = f'{self.path}/required_files'

        fixtures = (
            (True, 'valid'),
            (False, 'invalid'),
        )

        for flag, name in fixtures:
            fixture = f'{flag}_{name}'
            with open(f'{path}/{fixture}_request.json') as file:
                data = json.load(file)

            files = {}
            file_path = data.get('file_path')

            if file_path is not None:
                with open(f'{self.files}/{file_path}', 'rb') as file:
                    files['resume'] = file

            returned_flag = required_files(
                files=files,
            )

            self.assertEqual(returned_flag, flag, msg=fixture)

    def test_is_email_valid(self):
        path = f'{self.path}/is_email_valid'

        fixtures = (
            (True, 'valid'),
            (False, 'invalid'),
        )

        for flag, name in fixtures:
            fixture = f'{flag}_{name}'
            with open(f'{path}/{fixture}_request.json') as file:
                email = json.load(file)

            returned_flag = is_email_valid(
                email=email,
            )

            self.assertEqual(returned_flag, flag, msg=fixture)

    def test_is_file_extension_valid(self):
        path = f'{self.path}/is_file_extension_valid'

        fixtures = (
            (True, 'valid'),
            (False, 'invalid'),
        )

        for flag, name in fixtures:
            fixture = f'{flag}_{name}'
            with open(f'{path}/{fixture}_request.json') as file:
                data = json.load(file)

            with open(f"{self.files}/{data['file_path']}", 'rb') as file:
                file = file

            returned_flag = is_file_extension_valid(
                file=file,
                extensions=data['valid_extensions'],
            )

            self.assertEqual(returned_flag, flag, msg=fixture)
