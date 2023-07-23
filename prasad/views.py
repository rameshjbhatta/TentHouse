from django.shortcuts import redirect, render
from django.http import HttpResponse
from prasad.magicform import ContactInfoForm

from prasad.models import FeedbackInfo

# Create your views here.


def index(request):
    return render(request,'prasad/index.html')

def about(request):
    return render(request,'prasad/about.html')

def home(request):
    return render(request,'prasad/index.html')

def services(request):
    return render(request,'prasad/services.html')

def gallery(request):
    return render(request, 'prasad/gallery.html')

def contact(request):
    if request.method =='POST':
        form = ContactInfoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('web_contact')
    else:
            form=ContactInfoForm()    
    return render(request, 'prasad/contact.html',{'form':form})




def feedback_handler(request):
    print("Hello world")
    if request.method =='POST':
        newvariable = request.POST['name']
        address = request.POST['address']
        email = request.POST['emailid']
        feedbacks = request.POST['customer_feedbacks']
        FeedbackInfo.objects.create(full_name=newvariable,address=address,email=email,feedback=feedbacks)
    detail= FeedbackInfo.objects.all()
           
    return render(request, 'prasad/feedback.html',{'detail':detail})


   