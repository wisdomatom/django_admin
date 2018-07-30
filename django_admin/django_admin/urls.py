"""django_admin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path

from App import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('load/', views.check_load),
    path('addauth/', views.addauth),
    path('addrole/', views.addrole),
    path('adduser/', views.adduser),
    path('addroleauth/', views.add_role_auth),
    path('adduserrole/', views.add_user_role),
    path('checkrole/', views.check_role),
    path('checkuser/', views.check_user),
    path('authrole/', views.auth_role),



]