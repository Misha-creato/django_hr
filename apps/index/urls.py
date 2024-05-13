from django.urls import path

from index.views import (
    IndexView,
    SendResponseView,
)


urlpatterns = [
    path(
        '',
        IndexView.as_view(),
        name='index',
    ),
    path(
        'send_response/<int:pk>',
        SendResponseView.as_view(),
        name='send_response',
    ),
]