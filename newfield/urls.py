from django.urls import path
from newfield.views import *

urlpatterns = [
    path('login/',loginClass.as_view(),name='login'),
    path('register/',registerClass.as_view(),name='register'),
    path('contact-form/',contactFormClass.as_view(),name='register'),
    path('custom-field/',customFieldClass.as_view(),name='register'),
]


