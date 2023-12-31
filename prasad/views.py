from django.shortcuts import redirect, render
from django.http import HttpResponse
from prasad.magicform import ContactInfoForm
from django.contrib import messages
from prasad.models import *
from rest_framework import viewsets, permissions
from django.contrib.auth.models import User
from .serializer import *
from django.core.paginator import Paginator
from django.shortcuts import render
from .models import ServiceInfo
import requests


def api_root(request):
    api_root_data = {
    "users": "http://127.0.0.1:8000/api/users/",
    "contactinfos": "http://127.0.0.1:8000/api/contactinfos/",
    "bookinginfos": "http://127.0.0.1:8000/api/bookinginfos/"
}
   # return JsonResponse(api_root_data)
    return render(request,'prasad/api_root.html',{'api_root_data':api_root_data})

# Create your viewsets here.
class ContactInfoViewSet(viewsets.ModelViewSet):
    queryset= ContactInfo.objects.all()
    serializer_class=ContactInfoSerializer
    permission_classes = [permissions.IsAuthenticated]

# inherits the behavior for handling various HTTP methods (GET, POST, PUT, DELETE) from the ModelViewSet class
class  BookingInfoViewSet(viewsets.ModelViewSet): 
    queryset = BookingInfo.objects.all()
    serializer_class = BookingInfoSerializer
    permission_classes = [permissions.IsAuthenticated] #accessible only to authenticated users (login users)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()   
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated] 

def ContactDataAPI(request):
    response = requests.get("http://127.0.0.1:8000/api/bookinginfos/")
    print(response)
    if response.status_code == '200':
        data = response.json()
        return render(request,'prasad/check.html',{'data':data})
    else:
       return HttpResponse('Please Log-In First')  #redirect to login page of admin for api access

def entrypage(request):
    return render(request, 'prasad/entrypage.html')


def about(request):
    return render(request, 'prasad/about.html')

def democontact(request):
    return render(request, 'prasad/democontact.html')

def index(request):
    images= GalleryHandler.objects.filter(img__icontains='tent')
    return render(request, 'prasad/index.html',{'images':images})

#pagination in service page

def services(request):
    #As the data is given through admin so no need to write POST method code 
    data = ServiceInfo.objects.all().order_by('title') #retrive data
    items_per_page = 4
    paginator = Paginator(data,items_per_page) #configure paginator
    current_page = request.GET.get('page',1) #get current page
    page = paginator.get_page(current_page)#get current page
    return render(request, 'prasad/services.html', {'page':page})  #parse data to template


def gallery(request):
    # Fetch all images from the database
    data = GalleryHandler.objects.all()
    return render(request, 'prasad/gallery.html', {'data': data})


def contact(request):
    if request.method == 'POST':
        form = ContactInfoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Message Posted Successfully')
            return redirect('web_contact')
        else:
            messages.error(request, 'Please enter the valid data')
    form = ContactInfoForm()
    return render(request, 'prasad/contact.html', {'form': form})


def booking_handler(request):
    if request.method == 'POST':
        newvariable = request.POST['name']
        bookingname = request.POST['bookingname']
        tentsize=request.POST['tentsize']
        eventname = request.POST['eventname']
        address = request.POST['address']
        email = request.POST['emailid']
        mobile=request.POST['mobile']
        eventday=request.POST['eventday']
        otherdetails = request.POST['otherdetails']
        BookingInfo.objects.create(
            full_name=newvariable, address=address, email=email,mobile_no=mobile,event_day_choice=eventday, other_details=otherdetails,booking_name=bookingname,event_name=eventname,tent_size=tentsize)
        if HttpResponse.status_code == 200:
            messages.success(request, 'Data submitted successfully!!')
        else:
            messages.warning(request, 'Please enter valid data')
    detail = BookingInfo.objects.all()
    return render(request, 'prasad/booking.html', {'detail': detail})


#search query
# from django.db.models import Q
# def search_handler(request):
#     query = request.GET.get('query')
#     results = None
#     if query:
#         # Implement your search logic here using the 'query' variable.
#         data = ServiceInfo.objects.filter(Q(title__icontains=query)|Q(img__icontains=query)|Q(content__icontains=query))
#         items_per_page = 2
#         paginator = Paginator(data,items_per_page) #configure paginator
#         current_page = request.GET.get('page') #get current page
#         results = paginator.get_page(current_page)#get current page
#     return render(request, 'prasad/services.html', {'query': query, 'results': results})

    

    
