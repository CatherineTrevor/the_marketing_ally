from django.db import models
from django.conf import settings
from phone_field import PhoneField


class QuoteRequest(models.Model):

    status_options = (
        ('1', 'Update consultation status'),
        ('2', 'No consultation requested'), 
        ('3', 'Consultation requested'),
        ('4', 'Consultation booked'),
    )

    company_name = models.CharField(max_length=50, null=False, blank=False)
    full_name = models.CharField(max_length=50, null=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone = PhoneField(blank=True)
    free_consultation_request = models.BooleanField()
    project_name = models.CharField(max_length=254)
    project_description = models.CharField(max_length=254)
    request_date = models.DateTimeField(auto_now_add=True)
    consultation_status = models.CharField(max_length=254, blank=True,
                                           choices=status_options, default=1)
    notes = models.TextField(blank=True)
