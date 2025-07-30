from django.shortcuts import render, redirect
from .forms import WebsiteForm, UserForm
from django.views.generic import View   
# Create your views here.

class WebsiteCreateView(View):
    def get(self, request, *args, **kwargs):
        form = WebsiteForm()
        context = {
            'form': form
        }
        return render(request, 'prueba_create_website.html', context)

    def post(self, request, *args, **kwargs):
        form = WebsiteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog:home')  # Redirect to a success page or home
        context = {
            'form': form
        }
        return render(request, 'prueba_create_website.html', context)

class UserFormView(View):
    def get(self, request, *args, **kwargs):
        form = UserForm()
        context = {
            'form': form
        }
        return render(request, 'prueba_user.html', context)

    def post(self, request, *args, **kwargs):
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog:home')  # Redirect to a success page or home
        context = {
            'form': form
        }
        return render(request, 'prueba_user.html', context)
