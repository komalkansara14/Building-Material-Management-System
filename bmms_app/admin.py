from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(UserRegistration)
admin.site.register(TransporterRegistration)
admin.site.register(GoDownStock)
admin.site.register(Price)
admin.site.register(Order)
admin.site.register(Transaction)
admin.site.register(ContactUs)
admin.site.register(PaidOrder)
admin.site.register(CompletedDelivery)