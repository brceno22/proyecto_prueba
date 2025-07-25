from django.urls import include, path
from . import views
from blog import views
from django.contrib import admin
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='/posts/')),  # Redirect root URL to posts
    path('posts/', views.lista_posts, name='lista_posts'),  # URL for listing posts
    
]      
       