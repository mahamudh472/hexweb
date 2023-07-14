from django import forms
from .models import *


class TimeInput(forms.TimeInput):
    input_type = 'time'

class DateInput(forms.DateInput):
    input_type = 'date'



class MembershipForm(forms.ModelForm):

    class Meta:

        model = Membership
        fields = ('start_date', 'country', 'referral_code')


class MembershipPersonForm(forms.ModelForm):

    class Meta:

        model = MembershipPerson
        fields = ('first_name', 'last_name', 'company', 'country_of_residence', 'email', 'phone_number', 'date_of_birth', 'gender', 'emergency_contact_name', 'emergency_contact_phone')
