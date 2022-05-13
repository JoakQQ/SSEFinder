from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.edit import UpdateView, DeleteView
from .models import CaseRecord
from .AddCaseRecord import CaseRecordForm


class CaseRecordView(ListView):
    template_name = "CaseRecord.html"
    model = CaseRecord


class CaseRecordUpdateView(UpdateView):
    model = CaseRecord
    fields = ["caseNumber", "personName", "identityDocumentNumber", "dateOfBirth","dateOfOnesetOfSymptoms","dateOfConfirmationOfInfectionByTesting"]
    template_name = 'CaseRecord_update.html'
    success_url = '/CaseRecord/Preview'


class CaseRecordDeleteView(DeleteView):
    model = CaseRecord
    template_name = 'CaseRecord_delete.html'
    success_url = '/CaseRecord'


def add_CaseRecord(request):
    if request.method == "GET":
        form = CaseRecordForm()
        return render(request, "AddCaseRecord.html", {"form": form})
    else:
        form = CaseRecordForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            CaseRecord.objects.create(**data)
            return redirect('CaseRecord')
        else:
            clear_errors = form.errors.get("__all__")
            return render(request, "AddCaseRecord.html", {"form": form, "clear_errors": clear_errors})
