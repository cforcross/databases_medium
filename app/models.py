from django.db import models

# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    principal = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    