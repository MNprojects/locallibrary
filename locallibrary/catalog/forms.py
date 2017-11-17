from django import forms

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
import datetime

class RenewBookForm(forms.Form):
    renewal_date = forms.DateField(help_text="Enter a date within the next 4 weeks")

    def clean_renewal_date(self):
        data = self.cleaned_data['renewal_date']
        #check if renewal date is in the past
        if data < datetime.date.today():
            raise ValidationError(_('Invalid date - renewal date is in the past'))
        #check if date is too far in the future
        if data > datetime.date.today() + datetime.timedelta(weeks=4):
            raise ValidationError(_('Invalid date - too far in the future'))
        #always need to return the cleaned data
        return data