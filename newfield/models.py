from datetime import datetime
from email.policy import default
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class contact(models.Model):
    tag_list = (
        ('birth','Birthday'),
        ('anv','Anniversary'),
        ('wed','Wedding'),
        ('pty','Party'),
        )

    timezone_list = (
        ('EST','Eastern Standard Time'),
        ('IST','India Standard Time'),
        ('ACT','Australian Central Time'),
        ('JST','Japan Standard Time'),
        )

    phone_no = models.CharField(max_length=10)
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    birthday = models.DateField()
    anniversary = models.DateField()
    tags = models.CharField(max_length = 20, choices = tag_list)
    override_timezone = models.DateField(max_length = 5, choices = timezone_list)


class custom_field(models.Model):
    type_list = (
        ('Text', 'Text'),
        ('Large Text', 'Large Text'),
        ('Date', 'Date'),
        ('Numerical', 'Numerical'),
    )

    field_name = models.CharField(max_length = 20)
    field_type = models.CharField(max_length = 15, choices = type_list)
    place_holder = models.CharField(max_length = 50)
    add_date = models.DateTimeField(default = datetime.now())
    agent_id = models.ForeignKey(User, default=None,on_delete=models.CASCADE,null=True)

class field_data(models.Model):
    custom_field_id = models.ForeignKey(custom_field,default=None, on_delete=models.CASCADE)
    contact_id = models.ForeignKey(contact,default=None, on_delete=models.CASCADE)
    field_data = models.TextField()