from django.contrib import admin
from prasad.models import *
from django.contrib import admin




class BookingInfoAdmin(admin.ModelAdmin):
    list_display= ['id','booking_name','event_name','full_name','address','mobile_no','event_day_choice','email','other_details']

class ContactInfoAdmin(admin.ModelAdmin):
    list_display= ['id','name','mobile','message']

class ServiceInfoAdmin(admin.ModelAdmin):
    list_display= ['sn','title','img','content']

class GalleryHandlerAdmin(admin.ModelAdmin):
    list_display=['id','img']   
    
admin.site.register(BookingInfo,BookingInfoAdmin)
admin.site.register(ContactInfo,ContactInfoAdmin)
admin.site.register(ServiceInfo,ServiceInfoAdmin)
admin.site.register(GalleryHandler,GalleryHandlerAdmin)



