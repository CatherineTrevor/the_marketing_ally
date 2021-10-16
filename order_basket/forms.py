from django import forms
from checkout.models import OrderRequest


class OrderRequestForm(forms.ModelForm):
    class Meta:
        model = OrderRequest
        read_only = ()
        fields = ('note')

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'note': 'note',
        }

        for field in self.fields:
            placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
