from django.http import JsonResponse
from django.views import View
from django.template.loader import render_to_string
from django.shortcuts import (
    render,
    redirect,
)

from index.services import (
    get_context_data,
    send_response,
    filter_vacancies,
)

from utils.constants import (
    EXPERIENCE_CHOICES,
    EMPLOYMENT_CHOICES,
    SCHEDULE_CHOICES,
)


class IndexView(View):
    def get(self, request, *args, **kwargs):
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            vacancies = filter_vacancies(
                request=request,
            )
            context = {
                'vacancies': vacancies,
                'EXPERIENCE_CHOICES': EXPERIENCE_CHOICES,
                'EMPLOYMENT_CHOICES': EMPLOYMENT_CHOICES,
                'SCHEDULE_CHOICES': SCHEDULE_CHOICES,
            }
            html = render_to_string(
                template_name="vacancies.html",
                context=context,
                request=request,
            )
            return JsonResponse(data=html, safe=False)
        else:
            context = get_context_data(
                request=request,
            )
        return render(
            request=request,
            template_name='index.html',
            context=context,
        )


class SendResponseView(View):
    def post(self, request, pk):
        send_response(
            request=request,
            pk=pk,
        )
        return redirect('index')
