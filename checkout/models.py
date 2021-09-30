import uuid

from django.db import models
from django.conf import settings

from datetime import datetime


class OrderRequest(models.Model):

    status_options = (
        ('1', 'Update order status'),
        ('2', 'Order timeslot requested'),
        ('3', 'Order timeslot confirmed'),
        ('4', 'Timeslot meeting completed and closed'),
    )

    id = models.CharField(max_length=50, null=False, primary_key=True, blank=False, default=False)
    account_company_name = models.CharField(max_length=50, null=False, blank=False)
    timeslot_option_1 = models.DateTimeField(default=datetime.now, blank=True)
    timeslot_option_2 = models.DateTimeField(default=datetime.now, blank=True)
    project_name = models.CharField(max_length=254, null=False, blank=False)
    project_description = models.CharField(max_length=254, null=False, blank=False)
    is_digital = models.BooleanField(default=False, null=False)
    total_booking_hours = models.CharField(max_length=254, null=False, blank=False)
    total_order_value = models.CharField(max_length=254, null=False, blank=False)
    order_status = models.CharField(max_length=254, null=False, blank=False, choices=status_options, default=1)
    order_timeslot_confirmed = models.BooleanField(default=False, null=False)

    def _generate_order_request_number(self):
        """
        Generate a random, unique order request number using UUID
        """
        return uuid.uuid4().hex.upper()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't been set already.
        """
        if not self.id:
            self.id = self._generate_order_request_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.id
