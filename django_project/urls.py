from django.contrib import admin
from django.urls import include, path
from . import views, settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
 
 

urlpatterns = [
    #path('', views.index, name='index'),
    path('', include('directory.urls')),
    path('admin/mypage',views.my_admin_view, name='my_admin_view'),
    path('admin/', admin.site.urls),
] 

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
