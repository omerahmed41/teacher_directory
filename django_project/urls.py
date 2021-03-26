from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    #path('', views.index, name='index'),
    path('', include('teacher_directory.urls')),
    path('admin/', admin.site.urls)
]
