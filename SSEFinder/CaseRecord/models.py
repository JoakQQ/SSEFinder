from django.db import models


class CaseRecord(models.Model):
    caseNumber = models.IntegerField()
    personName = models.CharField(max_length=200)
    identityDocumentNumber = models.CharField(max_length=200)
    dateOfBirth = models.DateField(auto_now_add=False)
    dateOfOnesetOfSymptoms = models.DateField(auto_now_add=False)
    dateOfConfirmationOfInfectionByTesting = models.DateField(auto_now_add=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.caseNumber)

    class Meta:
        ordering = ['-date']
