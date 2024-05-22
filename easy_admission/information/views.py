from django.shortcuts import render, redirect
from django.views.generic import View
from . models import ApplicatinCondition, Prospectus, Notices, ResultSheet, GotSubject, ApplyInformation
from accounts.models import ProfileModel
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

# Create your views here.

class ApplicationCondition(View):
    def get(self, request, *args, **kwargs):
        
        unit = kwargs.get('A')
        # print(unit)
        application = ApplicatinCondition.objects.filter(UnitName=unit).first()
        # print("====app==",application.Taka)
        context = {"unitS":unit, "applications":application}
        return render(request, 'application_condition.html', context)
    
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

            # print("sci_sit===========================", sci_sit)

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
    def get(self, request, *args, **kwargs):
        unit = kwargs.get('A')
        prospectus = Prospectus.objects.filter(unit=unit).order_by('-uploaded_at').first()
        context = {"unitS":unit, "prospectus":prospectus}
        print("yes pdf", prospectus.pdf_file)
        return render(request, 'prospectus_student.html',context)
    
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
    def get(self, request, *args, **kwargs):
        unit = kwargs.get('A')
        notice = Notices.objects.filter(unit=unit).order_by('-uploaded_at')
        context = {"unitS":unit, "notice":notice}
        return render(request, 'notices_student.html',context)

    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            title = request.POST.get('notice_title')
            notice = request.FILES['notice_pdf']
            unit = request.POST.get('UnitName')
            users = request.user

            noticeinstance, created = Notices.objects.get_or_create(
                    user=users,
                    notice = notice,
                    unit=unit,
                    title = title
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


def subjectStatus(request):
   
    students = GotSubject.objects.all()
    
   
    subjects = students.values_list('subject', flat=True).distinct()
    
  
    grouped_students = {}
    for subject in subjects:
     
        genders = students.filter(subject=subject).values_list('gender', flat=True).distinct()
        
        
        grouped_students[subject] = {}
        for gender in genders:
            grouped_students[subject][gender] = students.filter(subject=subject, gender=gender)
    
    return render(request, 'template.html', {'grouped_students': grouped_students})


class  MakeAdmid(View):
    pass



class NoticeDetail(View):
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        notice = Notices.objects.get(id=pk)
        context = {"flag":"flag", "notice":notice}
        return render(request, 'notices_student.html',context)


class Apply(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'apply.html')

    def post(self, request, *args, **kwargs):

        username = request.POST.get("username")
        password = request.POST.get("password")
        unit = request.POST.get("unit")

        user = authenticate(request, username=username, password=password)
            
            
        if user is not None:
            print("user authenticatons")
            profile  = ProfileModel.objects.filter(user=user).first()

            if profile:
                Apply, created = ApplyInformation.objects.get_or_create(
                user = user, 
                unit = unit, 
                  )
                Apply.save()
                context = {"massege":"Apply Successfully Completed, Please Payment Within 24 Hours!"}
                return render(request, 'student_toggle_dashboard.html', context)
            else:            
                return redirect('student_profile_update', pk=user.id )
        else:
            return redirect('register')


class Payment(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'payment.html')

    def post(self, request, *args, **kwargs):
        username = request.POST.get("username")
        user = User.objects.filter(username=username).first()

        if user is not None:
            apply_info = ApplyInformation.objects.filter(user=user).first()
            if apply_info:
                # Update the transactions field to True
                apply_info.transactions = True
                apply_info.save()

                # Optionally, you can add a message or redirect to a success page
                context = {"massege": "Payment processed successfully!"}
                return render(request, 'student_toggle_dashboard.html', context)
            else:
                # Handle case where apply_info is not found
                context = {"error": "Apply information not found for the user."}
                return render(request, 'payment.html', context)
        else:
            # Handle case where user is not found
            context = {"error": "User not found."}
            return render(request, 'payment.html', context)