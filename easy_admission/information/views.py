from django.shortcuts import render, redirect
from django.views.generic import View
from . models import ApplicatinCondition

# Create your views here.

class ApplicationCondition(View):
    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            # Retrieve data from POST request
            unit_name = request.POST.get('UnitName')
            taka = request.POST.get('Taka')
            first_date = request.POST.get('firstdate')
            last_date = request.POST.get('lastdate')
            total_site = request.POST.get('totalsit')
            sci_sit = request.POST.get('sci_sit')
            arts_sit = request.POST.get('arts_sit')
            com_sit = request.POST.get('com_sit')
            tec_adu_sit = request.POST.get('tec_adu_sit')
            sci_qua = request.POST.get('sci_qua')
            arts_qua = request.POST.get('arts_qua')
            com_qua = request.POST.get('com_qua')
            tec_qua = request.POST.get('tec_qua')

            # Get or create the object using the retrieved data

            print("sci_sit===========================", sci_sit)

            application, created = ApplicatinCondition.objects.get_or_create(
                UnitName=unit_name,
                Taka=taka,
                firstdate=first_date,
                lastdate=last_date,
                totalsit=total_site,
                sci_sit=sci_sit,
                arts_sit=arts_sit,
                com_sit=com_sit,
                tec_adu_sit=tec_adu_sit,
                sci_qua=sci_qua,
                arts_qua=arts_qua,
                com_qua=com_qua,
                tec_qua=tec_qua,
                user = request.user
            )

            application.save()

        return redirect('teacherroom', pk=request.user.id)




