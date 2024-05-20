from django.shortcuts import render
from django.views.generic import View
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .forms import UserForm, UserLogInForm, ProfileForm, TeacherProfileForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from . models import UserAccountTypes, ProfileModel, TeacherProfileModel, profileImage
from django.http import HttpResponseNotFound
from django.urls import reverse

# Create your views here.

def home(request):
    return render(request, 'home.html')

# home page views end here.......................................................

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


# user registration ended here basicaly all kinds of user created here..


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

# user Lonin  ended here basicaly all kinds of user login here..

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


       
       

        if not profile:
            if acc_type.account_type=="student":
                return redirect('create_profile')  
            else:
                return redirect('create_teacher_profile')
         
        profile_photo = profileImage.objects.filter(user = profile.user).first()      
        
        if acc_type.account_type == 'student':
            return render(request, 'profile_student.html', {'profile':profile, 'profile_photo':profile_photo, 'user': users})
        else:
            return render(request, 'profile_teacher.html', {'profile':profile, 'profile_photo':profile_photo, 'user': users})


class CreateProfile(View):
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        user = User.objects.filter(pk=pk).first()
        profile_data = ProfileModel.objects.filter(user=user).first()
        profile = ProfileForm()
        profile_photo = profileImage.objects.filter(user=user).first()

       
        if not profile_data:
            return render(request, 'create_profile.html', {'profile':profile})
        else:
             return render(request, 'student_profile_update.html', {'profile':profile, 'profile_info':profile_data, 'profile_photo':profile_photo})


    def post(self, request, *args, **kwargs):
     
        if request.method == 'POST':
            
            form = ProfileForm(request.POST, request.FILES)
            print(form)
            if form.is_valid():
               
                profile = ProfileModel.objects.filter(user=request.user).first()
                profile_imgs = profileImage.objects.filter(user=request.user).first()
                
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



class StudentProfileUpdate(View):
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        user = User.objects.get(pk=pk)
        profile_data = ProfileModel.objects.filter(user=user).first()
        profile = ProfileForm()
        profile_photo = profileImage.objects.filter(user=user).first()
       
        if not profile_data:
            return render(request, 'create_profile.html', {'profile':profile})
        else:
             return render(request, 'student_profile_update.html', {'profile':profile, 'profile_info':profile_data, 'profile_photo':profile_photo})


    def post(self, request, *args, **kwargs):
        # Get the form data
        pk = kwargs.get('pk')
        print("pk==============", pk)
        full_name = request.POST.get('full_name')
        father_name = request.POST.get('father_name')
        mother_name = request.POST.get('mother_name')
        village = request.POST.get('village')
        subdistrict = request.POST.get('subdistrict')  
        district = request.POST.get('district')
        registration = request.POST.get('registration')
        ssc_year = request.POST.get('ssc_year')
        ssc_result = request.POST.get('ssc_result')
        ssc_board = request.POST.get('ssc_board')
        hsc_year = request.POST.get('hsc_year')
        hsc_result = request.POST.get('hsc_result')
        hsc_board = request.POST.get('hsc_board')
        user = User.objects.get(pk=pk)
        student = ProfileModel.objects.filter(user=user).first()

        image = request.FILES.get('image')

        print(image,"-----------==========")

        if student:
            student.full_name = full_name
            student.father_name = father_name
            student.mother_name = mother_name
            student.village = village
            student.subdistrict = subdistrict
            student.district = district
            student.registration = registration
            student.ssc_year = ssc_year
            student.ssc_result = ssc_result
            student.ssc_board = ssc_board
            student.hsc_year = hsc_year
            student.hsc_result = hsc_result
            student.hsc_board = hsc_board
            student.save()
        
       
        if image: 
            profile_photo, created = profileImage.objects.get_or_create(user=user)
            profile_photo.profile_image = image  
            profile_photo.save()




        return redirect('profile', pk=request.user.id)




class TeacherProfileUpdate(View):
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        user = User.objects.get(pk=pk)
        profile_data = TeacherProfileModel.objects.filter(user=user).first()
        profile = TeacherProfileForm()
        profile_photo = profileImage.objects.filter(user=user).first()
       
        if not profile_data:
            return render(request, 'create_profile.html', {'profile':profile})
        else:
             return render(request, 'teacher_profile_update.html', {'profile':profile, 'profile_info':profile_data, 'profile_photo':profile_photo})


    def post(self, request, *args, **kwargs):
        # Get the form data
        pk = kwargs.get('pk')
        print("pk==============", pk)
        full_name = request.POST.get('full_name')
        title = request.POST.get('title')
        phd = request.POST.get('phd')
        dept = request.POST.get('dept')
        village = request.POST.get('village')
        subdistrict = request.POST.get('subdistrict')  
        district = request.POST.get('district')
        cur_village = request.POST.get('cur_village')
        cur_subdistrict = request.POST.get('cur_subdistrict')
        cur_district = request.POST.get('cur_district')

      
        user = User.objects.get(pk=pk)
        teacher = TeacherProfileModel.objects.filter(user=user).first()

        image = request.FILES.get('image')

        

        if teacher:
            teacher.full_name = full_name
            teacher.title = title
            teacher.phd = phd
            teacher.dept = dept
            teacher.village = village
            teacher.subdistrict = subdistrict
            teacher.district = district

            teacher.cur_village = cur_village
            teacher.cur_subdistrict = cur_subdistrict
            teacher.cur_district = cur_district
           
            teacher.save()
        
       
        if image: 
            profile_photo, created = profileImage.objects.get_or_create(user=user)
            profile_photo.profile_image = image  
            profile_photo.save()




        return redirect('profile', pk=request.user.id)






class UserDeleteView(View):
    def get(self, request, pk):

        user = User.objects.get(pk=pk)
        if request.user.id == pk:
             user.delete()
        return redirect('home')


class TeacherDashboardView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'teacher_toggle_dashboard.html')
    
class StudentDashboardView(View):
    def get(self, request, *args, **kwargs):
        context = {"hello":"oi"}   
        return render(request, 'student_toggle_dashboard.html',context)

