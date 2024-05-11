from django.urls import path

from . import views
from .views import ApplicationCondition


urlpatterns = [
   path('make/application/condition/', ApplicationCondition.as_view(), name='application_condition'),
]