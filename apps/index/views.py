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


class IndexView(View):
    def get(self, request, *args, **kwargs):
        context = get_context_data(
            request=request,
        )
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            context['vacancies'] = filter_vacancies(
                request=request,
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
        send_response(
            request=request,
            pk=pk,
        )
        return redirect('index')
