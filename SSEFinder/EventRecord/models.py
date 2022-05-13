from django.db import models

class Event(models.Model):
    venueName = models.CharField(max_length=100)
    venueLocation = models.CharField(max_length=100)
    venueAddress = models.CharField(max_length=200)
    xCoord = models.FloatField()
    yCoord = models.FloatField()
    # eventDate = models.DateField(auto_now=False, auto_now_add=False)
    # description = models.CharField(max_length=500)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # return f'{self.venueName} ({self.xCoord}, {self.yCoord}) {self.eventDate}'
        return f'{self.venueName}, {self.venueLocation}, {self.venueAddress}, ({self.xCoord}, {self.yCoord})'

    class Meta:
        ordering = ['-date']
