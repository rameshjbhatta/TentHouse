from django.db import models

# Create your models here.
class FeedbackInfo(models.Model):
    full_name = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    feedback = models.TextField()

def __str__ (self):
    return self.full_name

class ContactInfo(models.Model):
    mobile = models.IntegerField()
    name = models.CharField(max_length=260)
    email = models.EmailField(max_length=260)
    subject = models.CharField(max_length=260)
    message = models.TextField(max_length=400)
    
    class Meta:
        db_table='contactinfo'
        
class ServiceInfo(models.Model):
    title=models.CharField(max_length=264)
    img=models.ImageField(upload_to='images', blank=True, null=True)
    
            
        
# class BookingInfo(models.Model):
#     full_name = models.CharField(max_length=100)
#     email = models.EmailField(blank=True, null=True)
#     phone_number = models.CharField(max_length=15)
#     event_date = models.DateField()
#     event_day=models.CharField(max_length=25)
#     tent_size = models.CharField(max_length=200)
#     additional_requirements = models.TextField(blank=True)

#     def __str__(self):
#         return f"{self.full_name} - {self.event_date}"     