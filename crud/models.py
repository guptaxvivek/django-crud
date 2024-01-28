from django.db import models

# Create your models here.

class INFOList(models.Model):
    name = models.CharField(max_length=255, blank=False, default='')
    email = models.EmailField(primary_key=True, null=False)
    phone = models.CharField(max_length=15, blank=False, default='')