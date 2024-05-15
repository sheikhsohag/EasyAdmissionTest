from django.urls import path

from . import views
from .views import ApplicationCondition, ProspectusView, NoticesView, MakeResult, PlaceSubject


urlpatterns = [
   path('make/application/condition/', ApplicationCondition.as_view(), name='application_condition'),
   path('make/Prospectus/', ProspectusView.as_view(), name='prospectus'),
   path('make/Notice/', NoticesView.as_view(), name='notice'),
   path('make/result/',MakeResult.as_view(), name='makeresult'),
   path('successful/placed/subject/',PlaceSubject.as_view(), name='gotsubject'),
]