from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from newfield.forms import *
# Create your views here.

class loginClass(View):
    template_name = "login.html"
    def get(self, request):
        return render(request, self.template_name)

class registerClass(View):
    template_name = 'register.html'
    def get(self, request):
        return render(request, self.template_name)

class customFieldClass(View):
    customField_form = customFieldForm
    template_name = 'customField.html'
    def get(self, request):
        return render(request, self.template_name, {'customFieldForm':self.customField_form})
    def post(self, request):
        formValue = customFieldForm(request.POST)
        # if formValue.is_valid():
        print(formValue)
        return HttpResponse(f'{formValue["field_name"].value()} {formValue["field_type"].value()} {formValue["place_holder"].value()}')
        return render(request, self.template_name, {'customFieldForm':self.customField_form})
    
class contactFormClass(View):
    contact_form = contactForm
    template_name = 'contactForm.html'
    def get(self, request):
        return render(request, self.template_name, {'contactForm':self.contact_form})
    
    def post(self, request):
        formValue = contactForm(request.POST)
        print(formValue)
        return HttpResponse(formValue)
        return render(request, self.template_name, {'contactForm':self.contact_form})
    