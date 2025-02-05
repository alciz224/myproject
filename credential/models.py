
# Create your models here.

from django.db import models

class Credential(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} ({self.code})"
