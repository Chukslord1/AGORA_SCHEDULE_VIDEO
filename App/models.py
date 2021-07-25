from django.db import models

# Create your models here.

class Meeting(models.Model):
    channel = models.TextField()
    meeting_title = models.TextField(null=True,blank=True)
    meeting_subject = models.TextField(null=True,blank=True)
    start_time = models.TimeField(null=True,blank=True)
    end_time = models.TimeField(null=True,blank=True)
    date = models.DateField(null=True,blank=True)

class Channel(models.Model):
    channel = models.TextField()
    app_id= models.TextField()
