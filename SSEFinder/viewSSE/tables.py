import django_tables2 as tables
from RelationshipRecord.models import Relationship


class SSETable(tables.Table):
    venueName = tables.Column(accessor='event.venueName', verbose_name='Venue name')
    venueLocation = tables.Column(accessor='event.venueLocation', verbose_name='Location')
    venueAddress = tables.Column(accessor='event.venueAddress', verbose_name='Address')
    xCoord = tables.Column(accessor='event.xCoord', verbose_name='x-coordinate')
    yCoord = tables.Column(accessor='event.yCoord', verbose_name='y-coordinate')
    detail = tables.TemplateColumn('<a href="{% url \'detail\' record.event.id record.eventDate start end %}">view detail</a>')
    class Meta:
        model = Relationship
        template_name = "django_tables2/bootstrap.html"
        fields = ('venueName',
                  'venueLocation',
                  'venueAddress',
                  'xCoord',
                  'yCoord',
                  'detail', )

class SSETableDetail(tables.Table):
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
                  'yCoord',)

class InfectorTable(tables.Table):
    caseNumber = tables.Column(accessor='case.caseNumber', verbose_name='Case number')
    personName = tables.Column(accessor='case.personName', verbose_name='Person name')
    identityDocumentNumber = tables.Column(accessor='case.identityDocumentNumber',
                                           verbose_name='Identity document number')
    dateOfBirth = tables.Column(accessor='case.dateOfBirth',
                                verbose_name='Date of birth')
    dateOfOnesetOfSymptoms = tables.Column(accessor='case.dateOfOnesetOfSymptoms',
                                           verbose_name='Date of onset of symptoms')
    dateOfConfirmationOfInfectionByTesting = tables.Column(accessor='case.dateOfConfirmationOfInfectionByTesting',
                                                           verbose_name='Date of confirmation of infection by testing')

    class Meta:
        model = Relationship
        template_name = "django_tables2/bootstrap.html"
        fields = ('caseNumber',
                  'personName',
                  'identityDocumentNumber',
                  'dateOfBirth',
                  'dateOfOnesetOfSymptoms',
                  'dateOfConfirmationOfInfectionByTesting',
                  'description',)


class InfectedTable(tables.Table):
    caseNumber = tables.Column(accessor='case.caseNumber', verbose_name='Case number')
    personName = tables.Column(accessor='case.personName', verbose_name='Person name')
    identityDocumentNumber = tables.Column(accessor='case.identityDocumentNumber',
                                           verbose_name='Identity document number')
    dateOfBirth = tables.Column(accessor='case.dateOfBirth',
                                verbose_name='Date of birth')
    dateOfOnesetOfSymptoms = tables.Column(accessor='case.dateOfOnesetOfSymptoms',
                                           verbose_name='Date of onset of symptoms')
    dateOfConfirmationOfInfectionByTesting = tables.Column(accessor='case.dateOfConfirmationOfInfectionByTesting',
                                                           verbose_name='Date of confirmation of infection by testing')

    class Meta:
        model = Relationship
        template_name = "django_tables2/bootstrap.html"
        fields = ('caseNumber',
                  'personName',
                  'identityDocumentNumber',
                  'dateOfBirth',
                  'dateOfOnesetOfSymptoms',
                  'dateOfConfirmationOfInfectionByTesting',
                  'description', )
