# Generated by Django 4.1.2 on 2022-10-11 05:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newfield', '0007_alter_contact_add_date_alter_contact_anniversary_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='add_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 11, 10, 53, 12, 956155)),
        ),
        migrations.AlterField(
            model_name='custom_field',
            name='add_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 11, 10, 53, 12, 956155)),
        ),
    ]