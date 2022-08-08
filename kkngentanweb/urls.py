from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),
    path('', include('website.urls', namespace = 'website')),
    path('ckeditor/',include('ckeditor_uploader.urls')),
]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)