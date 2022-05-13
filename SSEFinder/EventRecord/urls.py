from django.urls import path
from EventRecord import views


urlpatterns = [
    path('',
        views.add_EventRecord,
        name="add_EventRecord"
    ),
    path('Preview',
        views.EventRecordView.as_view(),
        name="EventRecord"
    ),
    path('update_VenueRecord/<slug:pk>',
        views.EventRecordUpdateView.as_view(),
        name="update_VenueRecord"
    ),
    path('delete_VenueRecord/<slug:pk>',
        views.EventRecordDeleteView.as_view(),
        name="delete_VenueRecord"
    ),
]
