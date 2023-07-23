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
        
      