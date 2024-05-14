import json
import os.path

from django.test import TestCase

from index.check import (
    required_data,
    required_files,
    is_email_valid,
    is_resume_valid,
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

            response = self.client.post(
                '/',
                data=data,
            )

            request = response.wsgi_request

            returned_flag = required_data(
                request=request,
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

            if data.get('file_path') is not None:
                data['resume'] = open(f"{self.files}/{data['file_path']}", 'rb')

            response = self.client.post(
                '/',
                data=data,
            )

            request = response.wsgi_request

            returned_flag = required_files(
                request=request,
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
                data = json.load(file)

            response = self.client.post(
                '/',
                data=data,
            )

            request = response.wsgi_request

            returned_flag = is_email_valid(
                request=request,
            )

            self.assertEqual(returned_flag, flag, msg=fixture)

    def test_is_resume_valid(self):
        path = f'{self.path}/is_resume_valid'

        fixtures = (
            (True, 'valid'),
            (False, 'invalid'),
        )

        for flag, name in fixtures:
            fixture = f'{flag}_{name}'
            with open(f'{path}/{fixture}_request.json') as file:
                data = json.load(file)

            data['resume'] = open(f"{self.files}/{data['file_path']}", 'rb')

            response = self.client.post(
                '/',
                data=data,
            )

            request = response.wsgi_request

            returned_flag = is_resume_valid(
                request=request,
            )

            self.assertEqual(returned_flag, flag, msg=fixture)

