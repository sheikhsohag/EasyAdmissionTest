from django.urls import path

from . import views
from .views import LoginViews, LogoutViews, Profile, CreateProfile, TeacherProfile,StudentProfileUpdate, UserDeleteView


urlpatterns = [
    path('', views.home, name="home"),
    path('register/', views.RegisterViews, name='register'),
   
    path('login/', LoginViews.as_view(), name='login'),
    path('logout/', LogoutViews.as_view(), name='logout'),
    path('profile/<int:pk>/', Profile.as_view(), name='profile'),
    path('profile/', Profile.as_view(), name='profile'),

    path('Createprofile/', CreateProfile.as_view(), name='create_profile'),
    path('Createprofile/<int:pk>', CreateProfile.as_view(), name='create_profile'),
    path('student/Update/profile/<int:pk>', StudentProfileUpdate.as_view(), name='student_profile_update'),
    path('user/delete/<int:pk>/', UserDeleteView.as_view(), name='user_delete'),

    path('Teacher/profile/', TeacherProfile.as_view(), name='create_teacher_profile'),
      
    # path('update/<int:pk>/', UserView.as_view(), name='update_user'),
    # path('delete/<int:pk>/', UserView.as_view(), name='delete_user'),
]