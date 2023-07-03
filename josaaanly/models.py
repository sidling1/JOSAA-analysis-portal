from django.db import models

# Create your models here.
class Data(models.Model):
    Institute = models.TextField()
    Programme = models.TextField()
    SeatType = models.TextField()
    Gender = models.TextField()
    OpeningRank = models.TextField()
    ClosingRank = models.TextField()
    Round = models.IntegerField()
    DualDeg = models.BooleanField()
    Year = models.IntegerField(default=0000)

