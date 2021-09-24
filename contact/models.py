from django.db import models
from django.conf import settings

class QuoteRequest(models.Model):
    company_name = models.CharField(max_length=50, null=False, blank=False)
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    free_consultation_request = models.BooleanField(default=False)
    project_name = models.CharField(max_length=254, null=False, blank=False)
    project_description = models.CharField(max_length=254, null=False, blank=False)    
