from django import forms
from EventRecord.models import Event
from CaseRecord.models import CaseRecord as Case
from RelationshipRecord.models import Relationship
from django.db import IntegrityError
from datetime import timedelta


class AddRelationshipRecordForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(AddRelationshipRecordForm, self).__init__(*args, **kwargs)
        self.fields['case'] = forms.ModelChoiceField(label='Case Number', queryset=Case.objects.all())
        self.fields['event'] = forms.ModelChoiceField(queryset=Event.objects.all())
        self.fields['eventDate'] = forms.DateField(label='Date of Event (MM/DD/YYYY or YYYY-MM-DD)')
        self.fields['description'] = forms.CharField(label='description',widget=forms.Textarea(attrs={"rows":15, "cols":100}))
        self.obj = None

    def save(self):
        matched_list = Relationship.objects.filter(case=self.cleaned_data['case'],
                                                   event=self.cleaned_data['event'],
                                                   eventDate=self.cleaned_data['eventDate'],
                                                   description=self.cleaned_data['description'])
        if len(matched_list) > 0:
            return 2

        r = self.cleaned_data['case']
        if self.cleaned_data['eventDate'] < r.dateOfOnesetOfSymptoms - timedelta(days=14):
            return 3
        elif self.cleaned_data['eventDate'] > r.dateOfConfirmationOfInfectionByTesting:
            return 3
        try:
            self.obj = Relationship.objects.create(case=self.cleaned_data['case'],
                                                   event=self.cleaned_data['event'],
                                                   eventDate=self.cleaned_data['eventDate'],
                                                   description=self.cleaned_data['description'])
            return 0
        except IntegrityError:
            return 1

    def get_obj(self):
        return self.obj

    class Meta:
        model = Relationship
        fields = ['case', 'event', 'eventDate', 'description']


class UpdateRelationshipRecordForm(forms.Form):
    def __init__(self, *args, obj_id=None):
        super(UpdateRelationshipRecordForm, self).__init__(*args)
        self.obj_id = obj_id
        self.obj = Relationship.objects.get(pk=self.obj_id)
        self.case_id = self.obj.case.id
        self.event_id = self.obj.event.id
        self.eventDate = self.obj.eventDate
        self.description = self.obj.description
        self.fields['case'] = forms.ModelChoiceField(label='Case Number', queryset=Case.objects.all(), initial=self.case_id)
        self.fields['event'] = forms.ModelChoiceField(queryset=Event.objects.all(), initial=self.event_id)
        self.fields['eventDate'] = forms.DateField(label='Date of Event (MM/DD/YYYY or YYYY-MM-DD)', initial=self.eventDate)
        self.fields['description'] = forms.CharField(label='description', initial=self.description)

    def save(self):
        new_case = self.cleaned_data['case']
        new_event = self.cleaned_data['event']
        new_eventDate = self.cleaned_data['eventDate']
        new_description = self.cleaned_data['description']

        matched_list = Relationship.objects.filter(case=new_case,
                                                   event=new_event,
                                                   eventDate=new_eventDate,
                                                   description=new_description)
        if len(matched_list) > 0:
            for r in matched_list:
                if r.pk != self.obj_id:
                    return 2

        if new_eventDate < new_case.dateOfOnesetOfSymptoms - timedelta(days=14):
            return 3
        elif new_eventDate > new_case.dateOfConfirmationOfInfectionByTesting:
            return 3

        try:
            obj = Relationship.objects.get(pk=self.obj_id)
            obj.case = new_case
            obj.event = new_event
            obj.eventDate = new_eventDate
            obj.description = new_description
            obj.save()
            self.obj = obj
            return 0
        except IntegrityError:
            return 1

    def get_obj(self):
        return self.obj

    class Meta:
        model = Relationship
        fields = ['case', 'event', 'eventDate', 'description']
