

from django.contrib import admin
from django.urls import path
from django.urls import include
from .views import HomeView
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('blog/', include('blog.urls', namespace='blog')),
    path('prueba/', include('prueba.urls', namespace='prueba')),
    
]
if settings.DEBUG:
    # Include django_browser_reload URLs only in DEBUG mode
    urlpatterns += [
        path("__reload__/", include("django_browser_reload.urls")),
    ]