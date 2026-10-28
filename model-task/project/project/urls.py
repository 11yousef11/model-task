from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from pages import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('index/', views.index),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
