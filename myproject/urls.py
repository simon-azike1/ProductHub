from django.contrib import admin
from django.urls import path, include
from .views import home  # home view in this file
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),              # Home page at root
    path('accounts/', include('accounts.urls')),  # Include accounts app URLs
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
