from django.db import models

# Create your models here.
class contactEnquiry(models.Model):
    name = models.CharField(max_length=80)
    email = models.CharField(max_length=80)
    message = models.TextField()