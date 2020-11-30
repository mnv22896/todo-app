

from django.db import models

# Create your models here.

from django.db import models
import datetime

from django.db import models
from django.utils import timezone


class List(models.Model):
    item = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    
    def __str__(self):
        return self.item