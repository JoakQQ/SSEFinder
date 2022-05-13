from django.urls import path
from RelationshipRecord import views


urlpatterns = [
    path('',
         views.AddRelationshipRecord.as_view(),
         name='add_RelationshipRecord'
         ),
    path('DeleteRelationshipRecord/<int:obj_id>',
         views.DeleteRelationshipRecord.as_view(),
         name='delete_RelationshipRecord'
         ),
    path('ConfirmRelationshipRecord/<int:obj_id>',
         views.ConfirmRelationshipRecord.as_view(),
         name='confirm_RelationshipRecord'
         ),
    path('UpdateRelationshipRecord/<int:obj_id>',
         views.UpdateRelationshipRecord.as_view(),
         name='update_RelationshipRecord'
         ),
]
