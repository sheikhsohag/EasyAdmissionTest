from django.urls import path

from . import views
from .views import ApplicationCondition, ProspectusView, NoticesView


urlpatterns = [
   path('make/application/condition/', ApplicationCondition.as_view(), name='application_condition'),
   path('make/Prospectus/', ProspectusView.as_view(), name='prospectus'),
   path('make/Notice/', NoticesView.as_view(), name='notice'),
]