from django.db import models
# from django.conf import settings


# Create your models here.
class Report(models.Model):
    shipper = models.FileField(upload_to='reports')


class Task(models.Model):
    task_id = models.CharField(max_length=100, null=False, blank=False)
