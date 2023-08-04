from django.db import models
from django.utils.text import slugify

# Create your models here.


class BookingInfo(models.Model):      
    EVENT_DAY_CHOICES = [
        ('one-day', 'One-day'),
        ('two-days', 'Two-days'),
        ('three-days', 'Three-days'),
        ('more', 'More'),
    ]

    booking_name = models.CharField(max_length=250)
    tent_size = models.CharField(max_length=250, null=True)
    event_name = models.CharField(max_length=250)
    full_name = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    email = models.EmailField(max_length=250, null=True)
    mobile_no = models.IntegerField()
    other_details = models.TextField()
    event_day_choice = models.CharField(
        max_length=20,
        choices=EVENT_DAY_CHOICES,
        default='one-day',
    )

class Meta:
            model = BookingInfo

def __str__(self):
       return f"{self.full_name} - {self.event_date}"




class ContactInfo(models.Model):
    mobile = models.IntegerField()
    name = models.CharField(max_length=260)
    message = models.TextField(max_length=400)
    
    class Meta:
        db_table='contactinfo'
        

class ServiceInfo(models.Model):
    sn = models.IntegerField(primary_key=True)
    title=models.CharField(max_length=264)
    img=models.ImageField(upload_to='images', blank=True, null=True)
    content =  models.TextField()
    slug = models.CharField(max_length=250,unique=True)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(ServiceInfo, self).save(*args, **kwargs)
    
class GalleryHandler(models.Model):
      img= models.ImageField(upload_to='images',blank=True,null=True)            
        
       