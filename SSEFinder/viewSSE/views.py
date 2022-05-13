from django.shortcuts import render
from RelationshipRecord.models import Relationship
from django_tables2.config import RequestConfig
from .tables import SSETable, InfectorTable, InfectedTable, SSETableDetail
from datetime import timedelta
from django.db import connection

def view_SSE(request):
    config = RequestConfig(request)
    queryStart = request.GET.get('start')
    queryEnd = request.GET.get('end')
    object_list1 = Relationship.objects.raw(
        '''SELECT * FROM(
        SELECT MAX(id) AS id, event_id, "eventDate"
        FROM "RelationshipRecord_relationship"
        WHERE "eventDate" BETWEEN '{0}' AND '{1}'
        GROUP BY event_id,"eventDate"
        HAVING COUNT(*)>7
        ORDER BY event_id) t JOIN "RelationshipRecord_relationship" r ON t.id=r.id
        '''.format(queryStart, queryEnd))

    if len(object_list1) != 0:
        check = True
    else:
        check = False

    table1 = SSETable(object_list1, prefix="1-")  # prefix specified
    config.configure(table1)

    return render(request, 'viewSSE.html', {
        'table1': table1,
        'check': check,
        'start': queryStart,
        'end': queryEnd,
    })


def view_detail(request, pk, date, start, end):
    config = RequestConfig(request)

    three_days_after_event = date + timedelta(days=3)
    two_days_after_event = date + timedelta(days=2)
    forteen_days_after_event = date + timedelta(days=14)


    event = Relationship.objects.raw(
        '''SELECT DISTINCT id,event_id
        FROM "RelationshipRecord_relationship"
        WHERE event_id = '{0}'
        LIMIT 1
        '''.format(pk))

    detailTableInfector = Relationship.objects.raw(
        '''
        SELECT *
        FROM "RelationshipRecord_relationship" AS R
        JOIN "CaseRecord_caserecord" AS C
        ON R.case_id = C.id
        AND R.event_id = '{0}'
        AND R."eventDate" = '{1}'
        WHERE C."dateOfOnesetOfSymptoms" <= '{2}'
        ORDER BY C."caseNumber"
        '''.format(pk, date.date(), three_days_after_event.date()))

    detailTableInfected = Relationship.objects.raw(
        '''
        SELECT *
        FROM "RelationshipRecord_relationship" AS R
        JOIN "CaseRecord_caserecord" AS C
        ON R.case_id = C.id
        AND R.event_id = '{0}'
        AND R."eventDate" = '{1}'
        WHERE C."dateOfOnesetOfSymptoms" BETWEEN '{2}' AND '{3}'
        ORDER BY C."caseNumber"
        '''.format(pk, date.date(), two_days_after_event.date(), forteen_days_after_event.date()))

    if len(detailTableInfector) != 0:
        check1 = True
    else:
        check1 = False

    if len(detailTableInfected) != 0:
        check2 = True
    else:
        check2 = False


    table1 = InfectorTable(detailTableInfector, prefix="1-")  # prefix specified
    config.configure(table1)
    table2 = InfectedTable(detailTableInfected, prefix="2-")  # prefix specified
    config.configure(table2)
    table3 = SSETableDetail(event, prefix="3-")
    config.configure(table3)

    return render(request, 'detailViewSSE.html', {
        'pk': pk,
        'date': date.date(),
        'start': start.date(),
        'end': end.date(),
        'table1': table1,
        'check1': check1,
        'table2': table2,
        'check2': check2,
        'table3': table3,
        'numCases': len(Relationship.objects.filter(event=pk, eventDate=date))
    })
