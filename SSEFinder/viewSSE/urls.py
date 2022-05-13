from django.urls import path, register_converter
from datetime import datetime
from viewSSE import views

class DateConverter:
    regex = '\d{4}-\d{2}-\d{2}'

    def to_python(self, value):
        return datetime.strptime(value, '%Y-%m-%d')

    def to_url(self, value):
        return value

register_converter(DateConverter, 'yyyy')

urlpatterns = [
    path('',
        views.view_SSE,
        name="viewSSE"
    ),
    path('<int:pk>/<yyyy:date>/<yyyy:start>/<yyyy:end>',
        views.view_detail,
        name="detail"
    ),
]
