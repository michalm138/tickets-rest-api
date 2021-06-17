from django.contrib import admin
from tickets_api import models

admin.site.register(models.Country)
admin.site.register(models.Company)
admin.site.register(models.Event)
admin.site.register(models.Ticket)
