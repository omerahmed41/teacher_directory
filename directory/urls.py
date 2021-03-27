from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('teatcher_import', views.teatcher_import, name='teatcher_import'),
    path('profile_upload', views.profile_upload, name='profile_upload'),
]


