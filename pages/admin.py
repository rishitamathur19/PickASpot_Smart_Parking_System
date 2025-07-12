from django.contrib import admin
from .models import registertable
from .models import usertable
# Register your models here.

class showusers(admin.ModelAdmin):
    list_display = ["name","email","phone","password"]

class showbookreq(admin.ModelAdmin):
    list_display = ["Name","Area", "Email","Phone","Date", "Time"]

admin.site.register(registertable,showusers)
admin.site.register(usertable,showbookreq)