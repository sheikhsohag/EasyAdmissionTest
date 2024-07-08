from django.urls import path

from . import views
from .views import *

urlpatterns = [
   path('make/application/condition/<str:A>/', ApplicationCondition.as_view(), name='application_condition'),
   path('make/Prospectus/<str:A>/', ProspectusView.as_view(), name='prospectus'),
   path('make/Notice/<str:A>/', NoticesView.as_view(), name='notice'),
   path('make/application/condition/', ApplicationCondition.as_view(), name='application_condition'),
   path('make/Prospectus/', ProspectusView.as_view(), name='prospectus'),
   path('make/Notice/', NoticesView.as_view(), name='notice'),
   path('make/result/',MakeResult.as_view(), name='makeresult'),
   path('successful/placed/subject/',PlaceSubject.as_view(), name='gotsubject'),
   path('take/admit_card/', MakeAdmid.as_view(), name="admit_card"),
   path('notice/details/<int:pk>/', NoticeDetail.as_view(), name="noticedetail"),
   path('apply/',Apply.as_view(), name="apply"),
   path('payment/', Payment.as_view(), name='payment'),
   path('admitcart/', AdmitCart.as_view(), name="admitcart"),
   path('result/', Result.as_view(), name="resultpb"),
   path('admitcart/date/', admitcartDate.as_view(), name="admitcartdate"),

   path('publish/result/', ResultView.as_view(), name="resultll"),
   path('publish/meritposition/',PublishMeritPosition.as_view(), name='publish_merit_position')
]