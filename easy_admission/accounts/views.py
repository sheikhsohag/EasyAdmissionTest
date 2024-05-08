from django.shortcuts import render
from django.views.generic import View
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .forms import UserForm, UserLogInForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from . models import User_Account

# Create your views here.

def home(request):
    return render(request, 'home.html')

def RegisterViews(request):
    if request.method == "POST":
        forms = UserForm(request.POST)
        if forms.is_valid():
            
            cleaned_data = forms.cleaned_data
        
            # Extract relevant data
            username = cleaned_data['username']
            first_name = cleaned_data['first_name']
            last_name = cleaned_data['last_name']
            email = cleaned_data['email']
            password1 = cleaned_data['password1']
            password2 = cleaned_data['password2']

            account_types = cleaned_data['account_type']


            user = User.objects.create_user(username=username, email=email, password=password1)
            user.first_name = first_name
            user.last_name = last_name
            userIn = user.save()
            
            user = User.objects.get(username=username)

            account_type_user = User_Account.objects.create(user=user, account_type=account_types)

            account_type_user.save()


            return redirect('login')  
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

