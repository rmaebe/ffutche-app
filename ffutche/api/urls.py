from django.contrib import admin
from django.urls import path
from django.urls import include
from ffutche import views
from django.contrib import admin
from ffutche.views import donor_create_view, app_create_view, parent_create_view
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ffutche.urls'))

]