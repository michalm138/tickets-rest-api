# Generated by Django 3.2.4 on 2021-06-17 19:56

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets_api', '0002_auto_20210617_2152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='representative_phone',
            field=models.CharField(max_length=45, validators=[django.core.validators.RegexValidator(message='Enter a valid value (e.g. +123456789 "+" - optional)', regex='^(\\+?\\d*)$')]),
        ),
    ]