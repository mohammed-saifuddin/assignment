from django.contrib import admin
from django.urls import path,include


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EmployeeDetailView



urlpatterns = [
     path('admin/', admin.site.urls),
    path("",include('project.urls')),
    
    
]