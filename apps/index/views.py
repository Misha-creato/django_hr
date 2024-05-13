from django.http import JsonResponse
from django.views import View
from django.template.loader import render_to_string
from django.shortcuts import (
    render,
    redirect,
)

from index.services import (
    get_context_data,
    get_vacancy,
    send_response,
    filter_vacancies,
)


class IndexView(View):
    def get(self, request, *args, **kwargs):
        context = get_context_data(
            request=request,
        )
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            context['vacancies'] = filter_vacancies(
                request=request,
                vacancies=context['vacancies'],
            )
            html = render_to_string(
                template_name="vacancies.html",
                context=context,
                request=request,
            )
            return JsonResponse(data=html, safe=False)
        return render(
            request=request,
            template_name='index.html',
            context=context,
        )


class SendResponseView(View):
    def post(self, request, pk):
        status, vacancy = get_vacancy(
            request=request,
            pk=pk,
        )
        if status == 200:
            send_response(
                request=request,
                vacancy=vacancy,
            )
        return redirect('index')
