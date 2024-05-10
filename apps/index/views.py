from django.shortcuts import render
from django.views import View

from index.services import get_context_data


class IndexView(View):
    def get(self, request, *args, **kwargs):
        context = get_context_data()
        return render(
            request=request,
            template_name='index.html',
            context=context,
        )
