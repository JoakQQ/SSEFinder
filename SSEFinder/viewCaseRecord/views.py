from django.shortcuts import render
from django_tables2.config import RequestConfig
from CaseRecord.models import CaseRecord
from RelationshipRecord.models import Relationship
from .tables import CaseTable, RelationshipTable
import requests

# Create your views here.
def view_case_try(request):
    config = RequestConfig(request)
    query = request.GET.get('q')
    object_list1 = CaseRecord.objects.filter(caseNumber = query)

    if len(object_list1) != 0:
        check1 = True
        object_list2 = Relationship.objects.filter(case=object_list1[0])
    else:
        check1 = False
        object_list2 = []

    if len(object_list2) != 0:
        check2 = True
    else:
        check2 = False

    table1 = CaseTable(object_list1, prefix="1-")  # prefix specified
    config.configure(table1)

    table2 = RelationshipTable(object_list2, prefix="2-")  # prefix specified
    config.configure(table2)

    return render(request, 'viewCase.html', {
        'table1': table1,
        'check1' : check1,
        'number' : query,
        'table2': table2,
        'check2' : check2,
    })
