from django import forms
from .models import OrderRequest


class OrderRequestForm(forms.ModelForm):
    class Meta:
        model = OrderRequest
        read_only = ()
        fields = ('account_company_name', 'timeslot_option_1',
                  'timeslot_option_1', 'project_name',
                  'project_description')

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'account_company_name': 'Company Name',
            'timeslot_option_1': 'Please enter a time',
            'timeslot_option_2': 'Please enter an alternative',
            'project_name': 'Project Name',
            'project_description': 'Project description',
        }

        for field in self.fields:
            placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
