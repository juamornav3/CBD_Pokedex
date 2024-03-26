
from django.contrib import admin
from django.urls import path
from pokecursor import views

urlpatterns = [
    path('', views.index),
    path('admin/', admin.site.urls),
    path('populate/', views.populate),
]
