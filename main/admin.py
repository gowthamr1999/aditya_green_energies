from django.contrib import admin
from .models import Service, Benefit , About, ContactInfo, ContactInquiry

admin.site.register(Service)
admin.site.register(Benefit)
admin.site.register(About)
admin.site.register(ContactInfo)
admin.site.register(ContactInquiry)