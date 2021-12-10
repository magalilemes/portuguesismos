from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('dicionario/', include('dicionario.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)