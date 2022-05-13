from django.urls import path
from viewCaseRecord import views


urlpatterns = [
    path('',
        views.view_case_try,
        name="viewCase"
    ),
]
