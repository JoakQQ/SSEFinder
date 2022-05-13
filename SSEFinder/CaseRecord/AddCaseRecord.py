from django.core.exceptions import ValidationError
from django import forms
from CaseRecord import models


class CaseRecordForm(forms.Form):
    caseNumber = forms.IntegerField(label="Case Number", error_messages={"required":"Pleas input the Case Number"})
    personName = forms.CharField(max_length=200,label="Person Name", error_messages={"required":"Pleas input the Person Name"})
    identityDocumentNumber = forms.CharField(max_length=200, label="Identity Document Number", error_messages={"required":"Pleas input the Identity Document Number"})
    dateOfBirth = forms.DateField(label="Date of Birth (MM/DD/YYYY)", error_messages={"required":"Pleas input the Date of Birth"})
    dateOfOnesetOfSymptoms = forms.DateField(label="Date of Oneset of Symptoms (MM/DD/YYYY)", error_messages={"required":"Pleas input the Date of Oneset of Symptoms"})
    dateOfConfirmationOfInfectionByTesting = forms.DateField(label="Date of Confirmation of Infection by Testing (MM/DD/YYYY)", error_messages={"required":"Pleas input the Date of Confirmation of Infection by Testing"})

    def __str__(self):
        return self.personName

    def clean_caseNumber(self):
        location = self.cleaned_data.get("caseNumber")

        if models.CaseRecord.objects.filter(caseNumber=location):
            raise ValidationError("Case Number already exist! ")
        else:
            return location

    def clean_identityDocumentNumber(self):
        location = self.cleaned_data.get("identityDocumentNumber")

        if models.CaseRecord.objects.filter(identityDocumentNumber=location):
            raise ValidationError("Identity Document Number already exist! ")
        else:
            return location
