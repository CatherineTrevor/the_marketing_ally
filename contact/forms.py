from django import forms
from .models import QuoteRequest


class QuoteRequestForm(forms.ModelForm):
    class Meta:
        model = QuoteRequest
        read_only = ()
        fields = ('company_name', 'full_name', 'email',
                  'phone', 'free_consultation_request', 'project_name',
                  'project_description')

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'company_name': 'Company Name',
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone': '',
            'free_consultation_request': None,
            'project_name': 'Project Name',
            'project_description': 'Project description',
        }

        for field in self.fields:
            placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            if not self.fields['free_consultation_request']:
                self.fields[field].label = False
