from django.urls import path
from CaseRecord import views

urlpatterns = [
    path('',
        views.add_CaseRecord,
        name="add_CaseRecord"
    ),
    path('Preview',
        views.CaseRecordView.as_view(),
        name="CaseRecord"
    ),
    path('update_CaseRecord/<slug:pk>',
        views.CaseRecordUpdateView.as_view(),
        name="update_CaseRecord"
    ),
    path('delete_CaseRecord/<slug:pk>',
        views.CaseRecordDeleteView.as_view(),
        name="delete_CaseRecord"
    ),


]
