from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from newfield.forms import *
from django.contrib.auth import authenticate, login, logout
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

# Create your views here.

class loginClass(View):
    template_name = "login.html"
    login_Form = loginForm
    def get(self, request):
        return render(request, self.template_name, {'loginForm':self.login_Form})
    def post(self, request):
        loginForm_data = loginForm(request.POST)
        if loginForm_data.is_valid():
            loginVerify = authenticate(request, username=loginForm_data['username'].value(), password=loginForm_data['password'].value())
            if loginVerify is not None:
                login(request, loginVerify)
                return HttpResponse("success")
        return render(request, self.template_name, {'loginForm':self.login_Form})



class registerClass(View):
    template_name = 'register.html'
    registerationForm = registerForm
    def get(self, request):
        return render(request, self.template_name,{'registerForm':self.registerationForm})
    def post(self, request):
        user_data = registerForm(request.POST)
        if user_data.is_valid():
            print(user_data)
            user_value = user_data.save()
            if user_value is not None:
                user_auth = authenticate(request, user_data['username'].value(),user_data['password'].value())
                if user_auth is not None:
                    login(request, user_auth)
            return HttpResponse('Success  ',user_value)
        return render(request, self.template_name,{'registerForm':self.registerationForm})



@method_decorator(login_required, name='dispatch')
class customFieldClass(View):
    customField_form = customFieldForm()
    template_name = 'customField.html'
    def get(self, request):
        return render(request, self.template_name, {'customFieldForm':self.customField_form})
    def post(self, request):
        formValue = customFieldForm(request.POST)
        # if formValue.is_valid():
        print(formValue)
        return HttpResponse(f'{formValue["field_name"].value()} {formValue["field_type"].value()} {formValue["place_holder"].value()}')
        return render(request, self.template_name, {'customFieldForm':self.customField_form})



@method_decorator(login_required, name='dispatch')
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


@method_decorator(login_required, name='dispatch')
class logoutClass(View):
    def get(self, request):
        logout(request)
        return redirect(loginClass.as_view())
