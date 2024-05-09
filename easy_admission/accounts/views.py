from django.shortcuts import render
from django.views.generic import View
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .forms import UserForm, UserLogInForm, ProfileForm, TeacherProfileForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from . models import UserAccountTypes, ProfileModel, TeacherProfileModel, profileImage

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

            account_type_user = UserAccountTypes.objects.create(user=user, account_type=account_types)

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

class Profile(View):
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        users = User.objects.filter(pk=pk).first()   
        acc_type = UserAccountTypes.objects.filter(user = users).first()
        
        if acc_type.account_type=="student":
            profile = ProfileModel.objects.filter(user=users).first()
        else:
            profile = TeacherProfileModel.objects.filter(user=users).first()


       
        print("==========================", profile, pk, users.username, acc_type.account_type)

        if not profile:
            if acc_type.account_type=="student":
                return redirect('create_profile')  
            else:
                return redirect('create_teacher_profile')
         
        profile_photo = profileImage.objects.filter(user = profile.user).first()      
        print(profile, profile_photo, acc_type)
        return render(request, 'profile_student.html', {'profile':profile, 'profile_photo':profile_photo, 'user': users})


class CreateProfile(View):
    def get(self, request, *args, **kwargs):
        profile = ProfileForm()
        return render(request, 'create_profile.html', {'profile':profile})

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = ProfileForm(request.POST, request.FILES)
            if form.is_valid():
                profile = ProfileModel.objects.filter(user=request.user).first()
                profile_imgs = profileImage.objects.filter(user=request.user).first()
                print("profile==============================")
                if profile:
                    profile.full_name = form.cleaned_data['full_name']
                    profile.father_name = form.cleaned_data['father_name']
                    profile.mother_name = form.cleaned_data['mother_name']
                    profile.village = form.cleaned_data['village']
                    profile.subdistrict = form.cleaned_data['subdistrict']
                    profile.district = form.cleaned_data['district']
                    profile.ssc_board = form.cleaned_data['ssc_board']
                    profile.ssc_year = form.cleaned_data['ssc_year']
                    profile.ssc_result = form.cleaned_data['ssc_result']
                    profile.registration = form.cleaned_data['registration']

                    profile.hsc_board = form.cleaned_data['hsc_board']
                    profile.hsc_year = form.cleaned_data['hsc_year']
                    profile.hsc_result = form.cleaned_data['hsc_result']
                    profile.save()

                else:
                    full_name = form.cleaned_data['full_name']
                    father_name = form.cleaned_data['father_name']
                    mother_name = form.cleaned_data['mother_name']
                    village = form.cleaned_data['village']
                    subdistrict = form.cleaned_data['subdistrict']
                    district = form.cleaned_data['district']
                    ssc_board = form.cleaned_data['ssc_board']
                    ssc_year = form.cleaned_data['ssc_year']
                    ssc_result = form.cleaned_data['ssc_result']
                    registration = form.cleaned_data['registration']

                    hsc_board = form.cleaned_data['hsc_board']
                    hsc_year = form.cleaned_data['hsc_year']
                    hsc_result = form.cleaned_data['hsc_result']

                    

                    print("imag ============link==========", profile_img)

                    profile = ProfileModel.objects.create(
                        full_name=full_name,
                        father_name=father_name,
                        mother_name=mother_name,
                        village=village,
                        subdistrict=subdistrict,
                        district=district,
                        ssc_board=ssc_board,
                        ssc_year=ssc_year,
                        ssc_result=ssc_result,
                        registration=registration,
                        hsc_board=hsc_board,
                        hsc_year=hsc_year,
                        hsc_result=hsc_result,
                        user=request.user  # Assuming the profile is associated with the current user
                    )

                if profile_imgs:
                    profile_imgs.profile_image = form.cleaned_data['profile_image']
                    profile_imgs.save()    

                else:
                    profile_img = form.cleaned_data['profile_image']
                    profile_pic = profileImage.objects.create(
                        user = request.user,
                        profile_image = profile_img
                        )

                    profile_pic.save()
                
                return redirect('profile', pk=request.user.id)

                
            else:
                # why form invalid this condition set later insha allah
                pass



class TeacherProfile(View):
    def get(self, request, *args, **kwargs):
        profile = TeacherProfileForm()
        return render(request, 'create_teacher_profile.html', {'profile':profile})

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = TeacherProfileForm(request.POST, request.FILES)
            if form.is_valid():
                profile =TeacherProfileModel.objects.filter(user=request.user).first()
                profile_imgs = profileImage.objects.filter(user=request.user).first()

                print("profile==============================")
                if profile:
                    profile.full_name = form.cleaned_data['full_name']
                    profile.title = form.cleaned_data['title']
                    profile.dept = form.cleaned_data['dept']
                    profile.phd = form.cleaned_data['phd']
                    profile.subdistrict = form.cleaned_data['subdistrict']
                    profile.district = form.cleaned_data['district']
                    profile.village = form.cleaned_data['village']
                    profile.cur_village = form.cleaned_data['cur_village']
                    profile.cur_subdistrict = form.cleaned_data['cur_subdistrict']
                    profile.cur_district = form.cleaned_data['cur_district']

                    profile.save()

                else:
                    full_name = form.cleaned_data['full_name']
                    title = form.cleaned_data['title']
                    dept = form.cleaned_data['dept']
                    village = form.cleaned_data['village']
                    subdistrict = form.cleaned_data['subdistrict']
                    district = form.cleaned_data['district']
                    cur_village = form.cleaned_data['cur_village']
                    cur_subdistrict = form.cleaned_data['cur_subdistrict']
                    cur_district = form.cleaned_data['cur_district']
                    phd = form.cleaned_data['phd']

                    

                    profile = TeacherProfileModel.objects.create(
                        full_name=full_name,
                        title=title,
                        dept=dept,
                        village=village,
                        subdistrict=subdistrict,
                        district=district,
                        cur_village=cur_village,
                        cur_subdistrict=cur_subdistrict,
                        cur_district=cur_district,
                        phd=phd,
                        
                        user=request.user  # Assuming the profile is associated with the current user
                    )

                    profile.save()

                if profile_imgs:
                    profile_imgs.profile_image = form.cleaned_data['profile_image']
                    profile_imgs.save()    

                else:
                    profile_img = form.cleaned_data['profile_image']
                    profile_pic = profileImage.objects.create(
                        user = request.user,
                        profile_image = profile_img
                        )

                    profile_pic.save()
                return redirect('profile', pk=request.user.id)

                
            else:
                # why form invalid this condition set later insha allah
                pass
        


