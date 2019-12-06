"""ffutche URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

from django.urls import path, include
from django.urls import include
from . import views
from django.contrib import admin
from ffutche.views import donor_create_view, app_create_view, parent_create_view
from django.contrib.auth import views as auth_views
from rest_framework import routers


router = routers.DefaultRouter()
router.register('donor', views.DonorView)
router.register('scholarship', views.ScholarshipView)
router.register('applicant', views.ApplicantView)
router.register('parent', views.ParentView)

urlpatterns = [
    path('Website.html', views.welcome, name='welcome'),
    path('Signin.html', views.login, name='Sign_in'),
    path('JoinUs.html', views.register, name='registration'),
    path('webportal.html', views.portal, name='web_portal'),
    path('scholarships.html', views.scholarships, name='scholarships'),
    path('admin/', admin.site.urls),
    path('Signin.html', auth_views.LoginView.as_view(template_name='Signin.html'), name='login'),
    path('applicant.html', app_create_view, name='registration'),
    path('parent.html', parent_create_view, name='parent'),
    path('donor.html', donor_create_view, name='donor'),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),


]
