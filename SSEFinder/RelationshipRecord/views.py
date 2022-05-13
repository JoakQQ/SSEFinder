from django.shortcuts import render, redirect
from django.views.generic import View, TemplateView
from django.contrib import messages
from RelationshipRecord.forms import AddRelationshipRecordForm, UpdateRelationshipRecordForm
from RelationshipRecord.models import Relationship


class AddRelationshipRecord(View):
    form_class = AddRelationshipRecordForm
    template_name = 'add_RelationshipRecord.html'

    def get(self, request):
        return render(request, self.template_name, {'form': self.form_class})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            ret_num = form.save()
            obj = form.get_obj()
            if ret_num == 3:
                messages.info(request, '*** Event date is not in period of interest ***')
                return redirect('add_RelationshipRecord')
            elif ret_num == 2:
                messages.info(request, '*** Relationship have already been added ***')
                return redirect('add_RelationshipRecord')
            elif ret_num == 1:
                messages.info(request, '*** Database Error ***')
                return redirect('add_RelationshipRecord')
            elif ret_num == 0:
                return redirect('confirm_RelationshipRecord', obj_id=obj.pk)
        else:
            return render(request, self.template_name, {'form': form})


class ConfirmRelationshipRecord(TemplateView):
    template_name = 'confirm_RelationshipRecord.html'

    def get_context_data(self, **kwargs):
        obj_id = self.kwargs['obj_id']
        obj = Relationship.objects.get(pk=obj_id)

        context = super().get_context_data(**kwargs)

        context['caseNumber'] = obj.case.caseNumber
        context['personName'] = obj.case.personName
        context['identityDocumentNumber'] = obj.case.identityDocumentNumber
        context['dateOfBirth'] = obj.case.dateOfBirth
        context['dateOfOnesetOfSymptoms'] = obj.case.dateOfOnesetOfSymptoms
        context['dateOfConfirmationOfInfectionByTesting'] = obj.case.dateOfConfirmationOfInfectionByTesting
        context['venue_name'] = obj.event.venueName
        context['venue_location'] = obj.event.venueLocation
        context['venue_address'] = obj.event.venueAddress
        context['x_coord'] = obj.event.xCoord
        context['y_coord'] = obj.event.yCoord
        context['event_date'] = obj.eventDate
        context['description'] = obj.description
        context['obj'] = obj

        return context


class DeleteRelationshipRecord(TemplateView):
    template_name = 'delete_RelationshipRecord.html'

    def get_context_data(self, **kwargs):
        obj_id = self.kwargs['obj_id']
        deleted_relationship = Relationship.objects.get(pk=obj_id)

        context = super().get_context_data(**kwargs)

        context['caseNumber'] = deleted_relationship.case.caseNumber
        context['venue_name'] = deleted_relationship.event.venueName
        context['venue_location'] = deleted_relationship.event.venueLocation
        context['venue_address'] = deleted_relationship.event.venueAddress
        context['x_coord'] = deleted_relationship.event.xCoord
        context['y_coord'] = deleted_relationship.event.yCoord
        context['event_date'] = deleted_relationship.eventDate
        context['description'] = deleted_relationship.description

        deleted_relationship.delete()

        return context


class UpdateRelationshipRecord(View):
    form_class = UpdateRelationshipRecordForm
    template_name = 'update_RelationshipRecord.html'

    def get(self, request, obj_id):
        self.form_class = UpdateRelationshipRecordForm(obj_id=obj_id)
        return render(request, self.template_name, {'form': self.form_class, 'obj_id': obj_id})

    def post(self, request, obj_id):
        form = self.form_class(request.POST, obj_id=obj_id)
        if form.is_valid():
            ret_num = form.save()
            obj = form.get_obj()
            if ret_num == 3:
                messages.info(request, '*** Event date is not in period of interest ***')
                return redirect('update_RelationshipRecord', obj_id=obj.pk)
            elif ret_num == 2:
                messages.info(request, '*** Relationship have already been added ***')
                return redirect('update_RelationshipRecord', obj_id=obj.pk)
            elif ret_num == 1:
                messages.info(request, '*** Database Error ***')
                return redirect('update_RelationshipRecord', obj_id=obj.pk)
            elif ret_num == 0:
                return redirect('confirm_RelationshipRecord', obj_id=obj.pk)
        else:
            return render(request, self.template_name, {'form': form, 'obj_id': obj_id})
