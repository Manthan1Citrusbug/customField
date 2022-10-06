from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from newfield.models import *
from django import forms
from django.core.exceptions import ValidationError

class registerForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

    def clean(self):
        password_one = self.cleaned_data.get['password1']
        password_two = self.cleaned_data.get['password2']
        email = self.cleaned_data.get['email']

        if password_one != None and password_two != None:
            if password_one != password_two:
                raise ValidationError('Both Passwords are not same')
        return self.cleaned_data

    def save(self, commit=True):
        user_data = super(registerForm, self).save(commit=False)
        user_data.email = self.cleaned_data['email']
        if commit:
            user_data.save()
        return user_data

class contactForm(forms.ModelForm):
    class Meta:
        model = contact
        fields = ['phone_no','first_name','last_name','birthday','anniversary','tags','override_timezone']
        labels = {
            'phone_no':'Phone No',
            'first_name':'First Name',
            'last_name':'Last Name',
            'birthday':'Birthday',
            'anniversary':'Anniversary',
            'tags':'Tags',
            'override_timezone':'Override Timezone',
        }
        widgets = {
            'phone_no': forms.TextInput(attrs = {'min_length':10, 'pattern':'[0-9]+'}),
        }

class customFieldForm(forms.ModelForm):
    class Meta:
        model = custom_field
        fields = ('field_name','field_type','place_holder')
        labels = {
            'field_name':'Field Name',
            'field_type':'Field Type',
            'place_holder':'Placeholder',
        }
