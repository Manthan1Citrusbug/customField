# Generated by Django 4.1.2 on 2022-10-21 07:06

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('newfield', '0011_alter_contact_add_date_alter_custom_field_add_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='add_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 21, 12, 36, 2, 601394)),
        ),
        migrations.AlterField(
            model_name='custom_field',
            name='add_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 21, 12, 36, 2, 601394)),
        ),
        migrations.AlterField(
            model_name='field_data',
            name='contact_id',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fields', to='newfield.contact'),
        ),
        migrations.AlterField(
            model_name='field_data',
            name='custom_field_id',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='newfield.custom_field'),
        ),
    ]