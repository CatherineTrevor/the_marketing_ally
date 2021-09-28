import uuid
import datetime

from django.db import models
from django.conf import settings


class QuoteRequest(models.Model):

    status_options = (
        ('1', 'Update consultation status'),
        ('2', 'No consultation requested'), 
        ('3', 'Consultation requested'),
        ('4', 'Consultation booked'),
    )

    quote_request_id = models.CharField(max_length=50, null=False, primary_key=True, blank=False, default=False)
    company_name = models.CharField(max_length=50, null=False, blank=False)
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    free_consultation_request = models.BooleanField(default=False, null=False)
    project_name = models.CharField(max_length=254, null=False, blank=False)
    project_description = models.CharField(max_length=254, null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    consultation_status = models.CharField(max_length=254, null=True, blank=True, choices=status_options, default=1)

    def _generate_quote_request_number(self):
        """
        Generate a random, unique quote request number using UUID
        """
        return uuid.uuid4().hex.upper()     

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't been set already.
        """
        if not self.quote_request_id:
            self.quote_request_id = self._generate_quote_request_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.quote_request_id
