from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    #path('', views.index, name='index'),
    path('', include('directory.urls')),
    path('admin/mypage',views.my_admin_view, name='my_admin_view'),
    path('admin/', admin.site.urls),
] 
