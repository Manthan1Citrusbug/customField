from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from newfield.models import *
from django import forms

class loginForm(forms.Form):
    username = forms.CharField(widget = forms.TextInput(attrs = {'placeholder':"Enter Username"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs = {'placeholder':"Enter Password"}), min_length = 8)

class registerForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
    
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
        widgets = {
            'phone_no': forms.TextInput(attrs = {'placeholder':'Enter Phone No','min_length':10, 'pattern':'[0-9]+'}),
            'first_name': forms.TextInput(attrs = {'placeholder':'Enter Firstname','pattern':'[a-zA-Z]+'}),
            'last_name': forms.TextInput(attrs = {'placeholder':'Enter Lastname','pattern':'[a-zA-Z]+'}),
            'birthday': forms.DateInput(attrs = {'class':'date_input', 'id':'rw_date_month3','placeholder':"mm-dd"}),
            'anniversary': forms.DateInput(attrs = {'class':'date_input', 'id':'rw_date_month4','placeholder':"mm-dd"}),
            'tags': forms.SelectMultiple(attrs = {'class':"js-states form-control",'id':"add_cont"}),
            'override_timezone': forms.Select(attrs = {'class':"js-states form-control"}),
        }

class customFieldForm(forms.ModelForm):
    class Meta:
        model = custom_field
        fields = ('field_name','field_type','place_holder')
        widgets = {
            'field_name': forms.TextInput(attrs={'placeholder':'eg: Event, Notes, Budget, Gender'}),
            'field_type': forms.RadioSelect(),
            'place_holder': forms.TextInput(attrs={'placeholder':'eg: Enter Event etc.'}),
        }
