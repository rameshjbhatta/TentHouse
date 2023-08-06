"""
URL configuration for RameshBhatta project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from prasad import views
from django.conf.urls.static import static
from rest_framework import routers
from prasad.views import api_root
from django.views.generic import TemplateView


admin.site.site_header = 'Biswash Tent House'
admin.site.index_title = 'Biswash Administration '

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'contactinfos',views.ContactInfoViewSet)
router.register(r'bookinginfos',views.BookingInfoViewSet)

urlpatterns = [
    
    path('api/', api_root, name='apipage'),
    path('api/',include(router.urls)),
    path('api-auth/',include('rest_framework.urls',namespace='rest_framework')),
    path('admin/', admin.site.urls),

# Here is no need to render data so simply redirect it to template using TemplateView class of Django
    path('', TemplateView.as_view(template_name='prasad/entrypage.html')),
    
    path('about/', TemplateView.as_view(template_name='prasad/about.html')),
 

#And for rendering data just direct it to the views and redirect to template with data
    path('home/',views.index, name='homepage' ),
    path('services/', views.services, name='web_services'),
    path('gallery/', views.gallery, name='web_gallery'),
    path('contact/', views.contact, name='web_contact'),
    path('contactAPI/', views.ContactDataAPI, name='web_contactAPI'),
    path('democontact/', views.democontact, name='democontact'),
    path('booking/', views.booking_handler, name='bookingpage'),
    # path('search/', views.search_handler, name='searchpage'),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
