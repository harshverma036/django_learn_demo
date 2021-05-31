from django.db import models

class StudentDetails(models.Model):
    name=models.CharField(max_length=70)
    stuClass = models.IntegerField()
    stuEmail = models.EmailField(max_length=70)