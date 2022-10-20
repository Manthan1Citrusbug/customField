from django.contrib import admin
from newfield.models import *
# Register your models here.

class CustomAdminClass(admin.ModelAdmin):
    list_display = ['id','phone_no','first_name','last_name','birthday','anniversary','tags', 'override_timezone','add_date','agent_id']

class CustomFieldAdminClass(admin.ModelAdmin):
    list_display =  ['id','field_name','field_type','place_holder','add_date','agent_id']

class FieldDataAdminClass(admin.ModelAdmin):
    list_display =  ['id','custom_field_id','contact_id','field_data']

admin.site.register(contact,CustomAdminClass)
admin.site.register(custom_field,CustomFieldAdminClass)
admin.site.register(field_data,FieldDataAdminClass)