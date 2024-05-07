from django.urls import path

from . import views
from .views import LoginViews, LogoutViews


urlpatterns = [
    path('', views.home, name="home"),
    path('register/', views.RegisterViews, name='register'),
   
    path('login/', LoginViews.as_view(), name='login'),
    path('logout/', LogoutViews.as_view(), name='logout'),
    # path('update/<int:pk>/', UserView.as_view(), name='update_user'),
    # path('delete/<int:pk>/', UserView.as_view(), name='delete_user'),
]