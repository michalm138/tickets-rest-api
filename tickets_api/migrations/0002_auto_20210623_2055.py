# Generated by Django 3.2.4 on 2021-06-23 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='description',
            field=models.TextField(default='No description'),
        ),
        migrations.AddField(
            model_name='event',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='event_image/'),
        ),
    ]
