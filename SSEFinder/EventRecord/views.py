from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.edit import UpdateView, DeleteView, FormView
from .models import Event
from .AddEventRecord import EventRecordForm
import requests
from datetime import datetime

class EventRecordView(ListView):
    template_name = "EventRecord.html"
    model = Event


class EventRecordUpdateView(UpdateView):
    model = Event
    fields = ["venueName","venueLocation","venueAddress","xCoord","yCoord"]
    # fields = ["venueName","venueLocation","venueAddress","xCoord","yCoord","eventDate","description"]
    template_name = 'EventRecord_update.html'
    success_url = '/VenueRecord/Preview'


class EventRecordDeleteView(DeleteView):
    model = Event
    template_name = 'EventRecord_delete.html'
    success_url = '/VenueRecord'

def get_location_api(name):
    # make the API Call
    r = requests.get('https://geodata.gov.hk/gs/api/v1.0.0/locationSearch?q=' + name)

    # check response code & handle it
    if r.status_code == 200:
        data = r.json()
        result = []
        result.append(200)
        for key in ['x', 'y', 'nameEN', 'addressEN']:
            result.append(data[0][key])
        return result
    else:
        return r.status_code, None

def add_EventRecord(request):
    if request.method == "GET":
        form = EventRecordForm()
        return render(request, "AddEventRecord.html", {"form": form})
    else:
        # create a form instance and populate it with data from the request:
        name = request.POST.get('venueLocation')

        form = EventRecordForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            answer = get_location_api(name)
            Event.objects.create(
                venueName = request.POST.get('venueName'),
                venueLocation = request.POST.get('venueLocation'),
                venueAddress = answer[4],
                xCoord = answer[1],
                yCoord = answer[2],
                # eventDate = request.POST.get('eventDate'),
                # eventDate = datetime.strptime(request.POST.get('eventDate'),'%m/%d/%Y'),
                # description = request.POST.get('description'),
                date = request.POST.get('date'))
            return redirect('EventRecord')
        else:
            clear_errors = form.errors.get("__all__")
            return render(request, "AddEventRecord.html", {"form": form, "clear_errors": clear_errors})
