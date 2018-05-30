from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.views.generic import RedirectView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', include('main.urls')),
    path('plants/', include('plants.urls')),
    path('gallery/', include('gallery.urls')),
    path('', RedirectView.as_view(url='/main/')),
    path('contact/', include('contact.urls')),
]