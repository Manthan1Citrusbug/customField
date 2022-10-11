from django.urls import path
from newfield.views import *

urlpatterns = [
    path('',loginClass.as_view(),name='login'),
    path('register/',registerClass.as_view(),name='register'),
    path('contact-form/',contactFormClass.as_view(),name='contactForm'),
    path('contact-form/<int:id>/',editContactClass.as_view(),name='editContact'),
    path('custom-field/',customFieldClass.as_view(),name='customField'),
    path('logout/',logoutClass.as_view(),name='logout'),

]


