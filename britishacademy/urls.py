# Define urlpatterns in project/urls.py
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from web import views
from django.views.generic import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('web.urls',namespace='web')),

    path('tinymce/', include('tinymce.urls')),
   
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "British Academy Administration"
admin.site.site_title = "British Academy Admin Portal"
admin.site.index_title = "Welcome to British Academy Admin Portal"

handler404 = views.handler404