from django.shortcuts import render
from django.views.generic import View
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .forms import UserForm, UserLogInForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

def home(request):
    return render(request, 'home.html')

def RegisterViews(request):
    if request.method == "POST":
        forms = UserForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('home')  
    else:
        forms = UserForm()
    return render(request, 'register.html', {'forms': forms})



class LoginViews(View):
   
    template_name = 'login.html'
  
    form_class = UserLogInForm
   
    
    def get(self, request, *args, **kwargs):       
        forms = self.form_class()
        return render(request, self.template_name, {'forms':forms})
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        
        if form.is_valid():
            
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            
            user = authenticate(request, username=username, password=password)
            
            
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                return redirect('register')
        else:
            return redirect('login')



class LogoutViews(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('home')

