from django.urls import include, path
from .views import WebsiteCreateView, UserFormView
app_name = 'prueba'
urlpatterns = [
    path('create/', WebsiteCreateView.as_view(), name='create'),
    path('user/', UserFormView.as_view(), name='user_form'),
]   