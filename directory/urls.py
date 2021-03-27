from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),  
    path('about', views.about, name='about'),
    path('teacher/<int:teacher_id>/', views.detail, name='detail'),
    path('import_CSV_file', views.import_CSV_file, name='profile_upload'),
]


