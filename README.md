
---
# Biswash Tent House Website Documentation
Biswash Tent House is the  Django project with a few applications (e.g., `prasad`) and their corresponding views, models, templates, and URL configurations. I'll provide a brief overview of the project structure and documentation for the main parts of the website:

 **Project Structure**:
   - The project consists of multiple Django applications, each handling specific functionalities.
   - The main application is named `prasad`, which appears to handle the core website.
   - Other applications include `rest_framework` for API views and `TemplateView` for rendering templates without passing data.

## Table of Contents
1. [Introduction](#introduction)
2. [Project Structure](#project-structure)
3. [Templates](#templates)
4. [Static Files](#static-files)
5. [Models](#models)
6. [Views](#views)
7. [URL Configurations](#url-configurations)
8. [REST API](#rest-api)
9. [Settings](#settings)
10. [Admin Panel](#admin-panel)

<a name="introduction"></a>
## 1. Introduction

Biswash Tent House is a Django-based website offering tent and event management services. This documentation provides an overview of the website's structure, components, and functionalities.

<a name="project-structure"></a>
## 2. Project Structure

The project consists of multiple Django applications, each handling specific functionalities. The main application is named `prasad`, and it contains the core website components.

```
project/
├── prasad/
│   ├── migrations/
│   ├── static/
│   │   ├── prasad/
│   │   │   ├── css/
│   │   │   │   ├── navbar.css
│   │   │   │   ├── logo.css
│   │   │   │   ├── about.css
│   │   │   │   ├── footerstyle.css
│   │   │   │   └── style.css
│   │   │   └── images/
│   │   │       ├── bdzlogo.png
│   │   │       ├── favicon.ico
│   │   │       ├── ...
│   │   │       └── tiktok.png
│   ├── templates/
│   │   └── prasad/
│   │       ├── entrypage.html
│   │       ├── about.html
│   │       ├── index.html
│   │       ├── services.html
│   │       ├── gallery.html
│   │       ├── contact.html
│   │       └── booking.html
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── ...
├── manage.py
└── requirements.txt
```

<a name="templates"></a>
## 3. Templates

The website uses Django templates to render HTML pages. These templates are located in the `prasad/templates/prasad/` directory. Here are the main templates used in the project:

1. `entrypage.html`: The main entry page of the website.
2. `about.html`: The page providing information about the website or the company.
3. `index.html`: The homepage of the website, displaying images and probably some information.
4. `services.html`: The page displaying services offered by the website.
5. `gallery.html`: The gallery page displaying images.
6. `contact.html`: The contact page with a contact form.
7. `booking.html`: The page to handle bookings and submission of booking data.

<a name="static-files"></a>
## 4. Static Files

The static files, including CSS stylesheets and images, are located in the `prasad/static/prasad/` directory. The website uses Bootstrap for styling.

<a name="models"></a>
## 5. Models

The website defines several models to manage data. The models are located in the `prasad/models.py` file. The main models are:

1. `BookingInfo`: Represents booking information for tent and event management services.
2. `ContactInfo`: Stores user contact information from the contact form.
3. `ServiceInfo`: Contains information about the services offered on the website.
4. `GalleryHandler`: Holds image data for the website's gallery.

<a name="views"></a>
## 6. Views

The views are defined in the `prasad/views.py` file. They handle different URL paths and render the corresponding templates. The views include functions for:

1. Rendering static pages (e.g., `index`, `about`, `services`, `gallery`, `contact`, `booking`).
2. Handling form submissions for contact and booking data.
3. API viewsets for the `ContactInfo`, `BookingInfo`, and `User` models.

<a name="url-configurations"></a>
## 7. URL Configurations

The URL patterns for the website are defined in the `prasad/urls.py` file. The URLs are associated with specific views and templates to be displayed.

<a name="rest-api"></a>
## 8. REST API

The project includes a REST API setup using Django REST framework. API endpoints and views are defined in `prasad/views.py`. The API root and URLs are configured in `prasad/urls.py`.

<a name="settings"></a>
## 9. Settings

The settings for the Django project are in the main `settings.py` file at the project level.

<a name="admin-panel"></a>
## 10. Admin Panel

The Django admin panel is accessible via the URL `/admin/`. It allows authorized users to manage data stored in the models.
