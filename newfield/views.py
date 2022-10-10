from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
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
                return JsonResponse({'success': 'custom-field/'})
            else:
                return JsonResponse({'error':'Enter correct Email or Password'})
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
        all_fields = custom_field.objects.all().filter(agent_id = request.user.id)
        fields_data = []
        for field in all_fields:
            field_data = {
                'name':field.field_name,
                'type':field.field_type,
                'place_holder':field.place_holder,
                'date':field.add_date,
            }
            fields_data.append(field_data)
        return render(request, self.template_name, {'customFieldForm':self.customField_form,'username':request.user.username, 'all_fields':fields_data})
    def post(self, request):
        formValue = customFieldForm(request.POST)
        if formValue.is_valid():
            check_field = custom_field.objects.filter(field_name=formValue["field_name"].value(), field_type = formValue["field_type"].value(), agent_id = request.user)
            if check_field.exists():
                return JsonResponse({'error':'This Field is already created'})
            else:
                currrent_obj = custom_field.objects.create(
                    field_name=formValue["field_name"].value(), 
                    field_type = formValue["field_type"].value(), 
                    place_holder = formValue["place_holder"].value(), 
                    agent_id = request.user
                )
                current_field_obj = custom_field.objects.get(id = currrent_obj.id)
                return JsonResponse({'success':'success'})
        return JsonResponse({'error':'Something Wrong Happened please try again'})
        return render(request, self.template_name, {'customFieldForm':self.customField_form})



@method_decorator(login_required(login_url=('../')), name='dispatch')
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


@method_decorator(login_required(login_url=('../')), name='dispatch')
class logoutClass(View):
    def get(self, request):
        logout(request)
        return redirect(loginClass.as_view())
