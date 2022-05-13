import django_tables2 as tables
from CaseRecord.models import CaseRecord
from RelationshipRecord.models import Relationship


class CaseTable(tables.Table):
    caseNumber = tables.Column(accessor='caseNumber', verbose_name='Case number')
    personName = tables.Column(accessor='personName', verbose_name='Person name')
    identityDocumentNumber = tables.Column(accessor='identityDocumentNumber',
                                           verbose_name='Identity document number')
    dateOfBirth = tables.Column(accessor='dateOfBirth',
                                verbose_name='Date of birth')
    dateOfOnesetOfSymptoms = tables.Column(accessor='dateOfOnesetOfSymptoms',
                                           verbose_name='Date of onset of symptoms')
    dateOfConfirmationOfInfectionByTesting = tables.Column(accessor='dateOfConfirmationOfInfectionByTesting',
                                                           verbose_name='Date of confirmation of infection by testing')
    class Meta:
        model = CaseRecord
        template_name = "django_tables2/bootstrap.html"
        fields = ('caseNumber', 
                  'personName',
                  'identityDocumentNumber',
                  'dateOfBirth',
                  'dateOfOnesetOfSymptoms',
                  'dateOfConfirmationOfInfectionByTesting', )


class RelationshipTable(tables.Table):
    venueName = tables.Column(accessor='event.venueName', verbose_name='Venue name')
    venueLocation = tables.Column(accessor='event.venueLocation', verbose_name='Location')
    venueAddress = tables.Column(accessor='event.venueAddress', verbose_name='Address')
    xCoord = tables.Column(accessor='event.xCoord', verbose_name='x-coordinate')
    yCoord = tables.Column(accessor='event.yCoord', verbose_name='y-coordinate')

    class Meta:
        model = Relationship
        template_name = "django_tables2/bootstrap.html"
        fields = ('venueName',
                  'venueLocation',
                  'venueAddress',
                  'xCoord',
                  'yCoord',
                  'description', )
