from django.contrib import admin
from prasad.models import *


# Register your models here.

class FeedbackInfoAdmin(admin.ModelAdmin):
    list_display= ['id','full_name','address','email','feedback']

class ContactInfoAdmin(admin.ModelAdmin):
    list_display= ['id','name','email','mobile','subject','message']
    
admin.site.register(FeedbackInfo,FeedbackInfoAdmin)
admin.site.register(ContactInfo,ContactInfoAdmin)



