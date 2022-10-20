from django.urls import path
from .views import *

urlpatterns = [
    path('custom-field/',api_custom_field.as_view(),name='api_custom_field'),
    path('contact-data/',api_contact.as_view(),name='api_contact'),
]


