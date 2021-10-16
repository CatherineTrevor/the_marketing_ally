from datetime import datetime
from django.db import models
from phone_field import PhoneField


class QuoteRequest(models.Model):

    status_options = (
        ('1', 'Update quote status'),
        ('2', 'Consultation requested'),
        ('3', 'Consultation booked, query closed'),
        ('4', 'Quote sent, query closed'),
    )
    id = models.BigAutoField(primary_key=True)
    company_name = models.CharField(max_length=50, null=False, blank=False)
    full_name = models.CharField(max_length=50, null=False)
    request_date = models.DateTimeField(default=datetime.now)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone = PhoneField(blank=True)
    free_consultation_request = models.BooleanField(blank=True, null=False)
    project_name = models.CharField(max_length=254, blank=True)
    project_description = models.CharField(max_length=254, blank=True)
    request_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=254, blank=True,
                              choices=status_options, default=1)
    query_closed = models.BooleanField(blank=True, null=True, default=False)
    notes = models.TextField(blank=True)

    def __str__(self):
        return self.company_name
