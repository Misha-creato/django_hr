import json
import os.path

from django.test import TestCase

from index.services import (
    get_vacancy,
    send_response,
)


CUR_DIR = os.path.dirname(__file__)


class ServicesTest(TestCase):
    fixtures = ['companies.json', 'vacancies.json']

    @classmethod
    def setUpTestData(cls):
        cls.path = f'{CUR_DIR}/fixtures/services'
        cls.files = f'{CUR_DIR}/fixtures/files'

    def test_get_vacancy(self):
        path = f'{self.path}/get_vacancy'
        response = self.client.get(
            '/',
        )

        request = response.wsgi_request

        fixtures = (
            (200, 'valid'),
            (404, 'not_found'),
        )

        for code, name in fixtures:
            fixture = f'{code}_{name}'
            with open(f'{path}/{fixture}_request.json') as file:
                pk = json.load(file)

            status_code, vacancy = get_vacancy(
                request=request,
                pk=pk,
            )

            self.assertEqual(status_code, code, msg=fixture)

    def test_send_response(self):
        path = f'{self.path}/send_response'

        fixtures = (
            (200, 'valid'),
            (400, 'invalid_email'),
            (400, 'invalid_file'),
            (400, 'required_email'),
            (400, 'required_resume'),
        )

        for code, name in fixtures:
            fixture = f'{code}_{name}'
            with open(f'{path}/{fixture}_request.json') as file:
                data = json.load(file)

            file_path = data.get('file_path')

            if file_path is not None:
                # with open(f"{self.files}/{file_path}", 'rb') as file:
                #     data['resume'] = file
                data['resume'] = open(f"{self.files}/{file_path}", 'rb')

            response = self.client.post(
                '/',
                data=data,
            )

            request = response.wsgi_request

            status_code = send_response(
                request=request,
                pk=1,
            )

            file = data.get('resume')
            if file:
                file.close()

            self.assertEqual(status_code, code, msg=fixture)
