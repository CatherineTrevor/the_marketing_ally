from django.db import models
from phone_field import PhoneField
from datetime import datetime


class QuoteRequest(models.Model):

    status_options = (
        ('1', 'Update quote status'),
        ('2', 'Consultation requested'),
        ('3', 'Consultation booked, query closed'),
        ('4', 'Quote sent, query closed'),
    )

    company_name = models.CharField(max_length=50, null=False, blank=False)
    full_name = models.CharField(max_length=50, null=False)
    request_date = models.DateTimeField(default=datetime.now)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone = PhoneField(blank=True)
    free_consultation_request = models.BooleanField()
    project_name = models.CharField(max_length=254)
    project_description = models.CharField(max_length=254)
    request_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=254, blank=True,
                              choices=status_options, default=1)
    query_closed = models.BooleanField()
    notes = models.TextField(blank=True)

    def __str__(self):
        return self.company_name
