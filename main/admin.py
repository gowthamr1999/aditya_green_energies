from django.contrib import admin
from .models import Service, Benefit , About, ContactInfo

admin.site.register(Service)
admin.site.register(Benefit)
admin.site.register(About)
admin.site.register(ContactInfo)