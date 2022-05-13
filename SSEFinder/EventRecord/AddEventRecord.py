from django.core.exceptions import ValidationError
from django import forms
from EventRecord import models


class EventRecordForm(forms.Form):
    venueName = forms.CharField(max_length=100, label="Venue Name", error_messages={"required":"Please input the venue name"})
    venueLocation = forms.CharField(max_length=100, label="Venue Location", error_messages={"required":"Please input the venue location"})
    # venueAddress = forms.CharField(max_length=200, label="Venue Address", error_messages={"required":"Please input the venue address"})
    # xCoord = forms.FloatField(label="X Coord", error_messages={"required":"Please input the X Coordinate"})
    # yCoord = forms.FloatField(label="Y Coord", error_messages={"required":"Please input the Y Coordinate"})
    # eventDate = forms.DateField(label="Event date", error_messages={"required":"Please input the event date"})
    # description = forms.CharField(max_length=500, label="Description", error_messages={"required":"Please input the description"})

    def __str__(self):
        return self.venueName

    def clean(self):
        super().clean()
        location1 = self.cleaned_data.get("venueName")
        location2 = self.cleaned_data.get("venueLocation")
        # location3 = self.cleaned_data.get("eventDate")

        # if (models.Event.objects.filter(venueName=location1)) and (models.Event.objects.filter(venueLocation=location2)) and (models.Event.objects.filter(eventDate=location3)):
        if (models.Event.objects.filter(venueName=location1)) and (models.Event.objects.filter(venueLocation=location2)):
            raise ValidationError("Event already exists!")
        else:
            return
