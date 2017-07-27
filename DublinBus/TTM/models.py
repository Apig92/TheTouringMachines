# This is a blueprint of the database
from django.db import models

class Routes(models.Model):
    RouteID = models.CharField(primary_key=True, max_length=5)
    BaseTime = models.DateTimeField()
    NumOfStop = models.IntegerField()

    def __str__(self):
        return self.RouteID + ' - ' + str(self.BaseTime) + ' - ' + str(self.NumOfStop)

class Stops(models.Model):
    StopID = models.IntegerField(primary_key=True)
    BusLine = models.ForeignKey(Routes, on_delete=models.CASCADE)
    Latitude = models.FloatField()
    Longitude = models.FloatField()
    TimeFromStart = models.DateTimeField()

    def __str__(self):
        return self.StopID + ' - ' + self.Latitude + self.Longitude
