from django.db import models
from CaseRecord.models import CaseRecord as Case
from EventRecord.models import Event


class Relationship(models.Model):
    case = models.ForeignKey(Case, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    eventDate = models.DateField(auto_now=False, auto_now_add=False)
    description = models.CharField(max_length=500)

    def __str__(self):
        return f'case: {self.case}, {self.event}, {self.eventDate}, {self.description}'
