from django.shortcuts import render, redirect
from django.views.generic import View
from . models import ApplicatinCondition, Prospectus, Notices, ResultSheet, GotSubject

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

class ProspectusView(View):
    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            pdf = request.FILES['pdf']
            unit = request.POST.get('UnitName')
            users = request.user

            pdfinstance, created = Prospectus.objects.get_or_create(
                    user=users,
                    pdf_file = pdf,
                    unit=unit
            )

            pdfinstance.save()

        return redirect('teacherroom', pk=request.user.id)

class NoticesView(View):
    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            notice = request.POST.get('notice')
            unit = request.POST.get('UnitName')
            users = request.user

            noticeinstance, created = Notices.objects.get_or_create(
                    user=users,
                    notice = notice,
                    unit=unit
            )

            noticeinstance.save()

        return redirect('teacherroom', pk=request.user.id)

class MakeResult(View):
    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            roll = request.POST.get('roll')
            obtain_mark = request.POST.get('obtain_mark')
            unit = request.POST.get('UnitName')
        
            result, created = ResultSheet.objects.get_or_create(
                roll = roll,
                obtain_mark = obtain_mark,
                unit = unit
            )

            result.save()
        return redirect('teacherroom', pk=request.user.id)



class PlaceSubject(View):
    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            roll = request.POST.get('roll')
            subject = request.POST.get('subject')
            unit = request.POST.get('unit')
            hall = request.POST.get('hallname')
            gender = request.POST.get('gender')
        
            subjectplace, created = GotSubject.objects.get_or_create(
                roll = roll,
                subject = subject,
                unit = unit,
                hall = hall,
                gender = gender
            )

            subjectplace.save()
        return redirect('teacherroom', pk=request.user.id)




