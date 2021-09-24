from django.db import models
from django.conf import settings

class Order(models.Model):
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    comment = models.EmailField(max_length=254, null=False, blank=False)    
