# Generated by Django 4.1.2 on 2022-10-11 05:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newfield', '0006_alter_contact_add_date_alter_contact_phone_no_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='add_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 11, 10, 38, 12, 988276)),
        ),
        migrations.AlterField(
            model_name='contact',
            name='anniversary',
            field=models.DateField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='birthday',
            field=models.DateField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='override_timezone',
            field=models.CharField(choices=[('EST', 'Eastern Standard Time'), ('IST', 'India Standard Time'), ('ACT', 'Australian Central Time'), ('JST', 'Japan Standard Time')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='tags',
            field=models.CharField(choices=[('birth', 'Birthday'), ('anv', 'Anniversary'), ('wed', 'Wedding'), ('pty', 'Party')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='custom_field',
            name='add_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 11, 10, 38, 12, 988276)),
        ),
        migrations.AlterField(
            model_name='field_data',
            name='field_data',
            field=models.TextField(default=None, null=True),
        ),
    ]
