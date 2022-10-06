from tkinter import CASCADE
from django.db import models

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
        ('CharField', 'Text'),
        ('TextField', 'Large Text'),
        ('DateField', 'Date'),
        ('IntegerField', 'Numerical'),
    )

    field_name = models.CharField(max_length = 20)
    field_type = models.CharField(max_length = 15, choices = type_list)
    place_holder = models.CharField(max_length = 50)
    customer_id = models.ForeignKey(contact, on_delete=models.CASCADE)

class field_data(models.Model):
    custom_field_id = models.ForeignKey(custom_field, on_delete=models.CASCADE)
    customer_id = models.ForeignKey(contact, on_delete=models.CASCADE)
    field_data = models.TextField()