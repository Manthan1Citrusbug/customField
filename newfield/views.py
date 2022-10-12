from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.views import View
import json
from newfield.forms import *
from newfield.models import *
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



@method_decorator(login_required(login_url=('../')), name='dispatch')
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
                custom_field.objects.create(
                    field_name=formValue["field_name"].value(), 
                    field_type = formValue["field_type"].value(), 
                    place_holder = formValue["place_holder"].value(), 
                    agent_id = request.user
                )
                return JsonResponse({'success':'success'})
        return JsonResponse({'error':'Something Wrong Happened please try again'})
        # return render(request, self.template_name, {'customFieldForm':self.customField_form})



@method_decorator(login_required(login_url=('../')), name='dispatch')
class contactFormClass(View):
    contact_form = contactForm
    template_name = 'contactForm.html'
    def get(self, request):
        all_fields = custom_field.objects.filter(agent_id = request.user.id)
        all_contact = contact.objects.filter(agent_id = request.user.id)
        return render(request, self.template_name, {'contactForm':self.contact_form,'username':request.user.username,'fields_data':all_fields,'contacts_data':all_contact})

    def post(self, request):
        formValue = json.loads(request.POST['data_value'])
        print("CONTACT-FORM:  ",formValue)
        if contact.objects.filter(phone_no = formValue["phone_no"]).exists():
            return JsonResponse({'success':False,'error':'This phone no is already added in system'})
        else:
            created_contact_id = contact.objects.create(
                phone_no=formValue["phone_no"], 
                first_name = formValue["first_name"],
                last_name = formValue["last_name"],
                birthday = formValue["birthday"],
                anniversary = formValue["anniversary"],
                tags = formValue["tags"],
                override_timezone = formValue["override_timezone"], 
                agent_id = request.user
            )
            if formValue['custom_fields']:
                custom_field_list = formValue['custom_fields']
                for current_field in custom_field_list:
                    custom_field_obj = custom_field.objects.get(pk=current_field[0])
                    field_data.objects.create(
                        contact_id = created_contact_id,
                        custom_field_id = custom_field_obj,
                        field_data = current_field[1]
                )
            return JsonResponse({'success':True})
        # return JsonResponse({'error':'Something Wrong Happened please try again'})
        # print(formValue)
        # return HttpResponse(formValue)
        # return render(request, self.template_name, {'contactForm':self.contact_form})
# document.getElementsByName("tags")[0].selectedOptions for getting value of multiple select 

@method_decorator(login_required(login_url=('../')), name='dispatch')
class editContactClass(View):
    def get(self, request, id):
            contacts_data = {}
            cur_contact = contact.objects.get(pk = id, agent_id = request.user)
            contacts_data['contact_id'] = cur_contact.id
            contacts_data['number'] = cur_contact.phone_no
            contacts_data['firstname'] = cur_contact.first_name
            contacts_data['lastname'] = cur_contact.last_name
            contacts_data['birthdate'] = cur_contact.birthday
            contacts_data['anniversary'] = cur_contact.anniversary
            contacts_data['tags'] = cur_contact.tags
            contacts_data['override_timezone'] = cur_contact.override_timezone
            all_fields = custom_field.objects.filter(agent_id = request.user)
            fields_data = []
            for field in all_fields:
                try:
                    field_data_value = field_data.objects.get(custom_field_id = field, contact_id = cur_contact)
                    cur_field = {
                        'name':field.field_name,
                        'value':field_data_value.field_data,
                    }
                except field_data.DoesNotExist:
                    cur_field = {
                        'name':field.field_name,
                        'value':"",
                    }
                fields_data.append(cur_field)

            contacts_data['user_fields'] = fields_data
            return JsonResponse({'success':'success','fields_data':contacts_data})
    
    def post(self, request):
        edit_data = json.loads(request.POST['data_value'])
        print("This is JSON Response data",edit_data)
        cur_contact = contact.objects.get(pk = edit_data['client_id'], agent_id = request.user)
        cur_contact.phone_no = edit_data['phone_no']
        cur_contact.first_name = edit_data['first_name']
        cur_contact.last_name = edit_data['last_name']
        cur_contact.birthday = edit_data['birthday']
        cur_contact.anniversary = edit_data['anniversary']
        cur_contact.tags = edit_data['tags']
        cur_contact.override_timezone = edit_data['override_timezone']
        cur_contact.save()

        all_fields = edit_data['custom_fields']
        for field in all_fields:
            cur_custom_field = custom_field.objects.get(pk=field[0], agent_id = request.user.id)
            try:
                field_data_value = field_data.objects.get(custom_field_id = cur_custom_field, contact_id = cur_contact)
                field_data_value.field_data = field[1]
                field_data_value.save()
            except field_data.DoesNotExist:
                field_data.objects.create(
                    contact_id = cur_contact,
                    custom_field_id = cur_custom_field,
                    field_data =  field[1]
                )
        
        return JsonResponse({'success':'success'})

@method_decorator(login_required(login_url=('../')), name='dispatch')
class logoutClass(View):
    def get(self, request):
        logout(request)
        return redirect("/")
