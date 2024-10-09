"""
URL configuration for event_management_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
'''from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]
'''
'''
from django.urls import include, path

urlpatterns = [
    path('', include('feedback.urls')),
]'''

"""
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

# A simple view for the home page (you can customize this later)
def home_view(request):
    return HttpResponse("Welcome to the Event Management System")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view),  # Add this to route the root URL to the home view
    path('feedback/', include('feedback.urls')),  # Keep your feedback app URLs
]
"""
'''
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('feedback/', include('feedback.urls')),  # Include the feedback app's URLs
]
'''
from django.contrib import admin
from django.urls import path, include
from feedback import views  # Import your feedback view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.feedback_view, name='feedback'),  # Root URL points to feedback view
    path('feedback/', include('feedback.urls')),  # Include the feedback app's URLs
]
