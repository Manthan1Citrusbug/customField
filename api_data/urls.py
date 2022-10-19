from django.urls import path
from .views import *

urlpatterns = [
    path('create-custom-field/',api_custom_field.as_view(),name='api_create_field')
]


