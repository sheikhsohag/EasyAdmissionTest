from django.shortcuts import render, redirect
from django.views.generic import View
from . models import ApplicatinCondition, Prospectus, Notices, ResultSheet, GotSubject, ApplyInformation, publishDate,MeritPosition
from accounts.models import ProfileModel
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.mixins import UserPassesTestMixin

from accounts.models import ProfileModel, profileImage
from sslcommerz_lib import SSLCOMMERZ 
from django.urls import reverse

from django.shortcuts import render, redirect
from django.views import View
from sslcommerz_lib import SSLCOMMERZ
from django.contrib.auth.models import User
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

import string, random
def transaction_id(size=10, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


class ApplicationCondition(View):


    def get(self, request, *args, **kwargs):
        unit = kwargs.get('A')
        application = ApplicatinCondition.objects.filter(UnitName=unit).first()
        context = {"unitS": unit, "applications": application}
        return render(request, 'application_condition.html', context)

    def post(self, request, *args, **kwargs):

        if not request.user.is_staff:
            return redirect('teacherroom', pk=request.user.id)
        
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
                user=request.user
            )

            application.save()
        context = {
            "message":"Application terms and condition created successfully!"
        }
        return redirect('teacherroom', pk=request.user.id)


class ProspectusView(View):
    def get(self, request, *args, **kwargs):
        unit = kwargs.get('A')
        prospectus = Prospectus.objects.filter(unit=unit).order_by('-uploaded_at').first()
        context = {"unitS":unit, "prospectus":prospectus}
        return render(request, 'prospectus_student.html',context)
    
    def post(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return redirect('teacherroom', pk=request.user.id)
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
        if not request.user.is_staff:
            return redirect('teacherroom', pk=request.user.id)
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
        if not request.user.is_staff:
            return redirect('teacherroom', pk=request.user.id)
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
        if not request.user.is_staff:
            return redirect('teacherroom', pk=request.user.id)
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

        if user:
            apply_info = ApplyInformation.objects.filter(user=user).first()
            if apply_info:
                # Update the transactions field to True
                apply_info.transactions = True
                apply_info.save()
                # Optionally, you can add a message or redirect to a success page

        if not user:
            return render(request, 'student_toggle_dashboard.html', {'error': 'User not found'})

        transaction = transaction_id()


        settings = { 
            'store_id': 'parce66569259986df', 
            'store_pass': 'parce66569259986df@ssl', 
            'issandbox': True 
        }
        sslcz = SSLCOMMERZ(settings)
        post_body = {
            'total_amount': 100.26,
            'currency': "BDT",
            'tran_id': transaction,
            'success_url': f'http://127.0.0.1:8000/information/payment/successfull/{transaction}/{user.id}/',
            'fail_url': "",
            'cancel_url': "",
            'emi_option': 0,
            'cus_name': "test",
            'cus_email': "test@test.com",
            'cus_phone': "01700000000",
            'cus_add1': "customer address",
            'cus_city': "Dhaka",
            'cus_country': "Bangladesh",
            'shipping_method': "NO",
            'multi_card_name': "",
            'num_of_item': 1,
            'product_name': "Test",
            'product_category': "Test Category",
            'product_profile': "general",
        }

        response = sslcz.createSession(post_body) # API response

        if response['status'] == 'SUCCESS':
            return redirect(response['GatewayPageURL'])
        else:
            return render(request, 'payment.html', {'error': 'Failed to create payment session'})






@csrf_exempt
def paymentsuccessful(request, trans, pk):
    user = User.objects.get(id=pk)
    
    if user:
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


        








        

class AdmitCart(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'admitCart_form.html')
    
    def post(self, request, *args, **kwargs):
        username = request.POST.get("username")
        password = request.POST.get("password")
        unit = request.POST.get("unit")

        user = authenticate(request, username=username, password=password)

        if user:
            apply = ApplyInformation.objects.filter(user=user).first()
            if apply is None:
                return render(request, 'student_toggle_dashboard.html', context={"massege":"You didn't Completed Admission Apply Proccess"})

            if apply.user:
            
                if apply.transactions:
                    applyInfo = ApplyInformation.objects.filter(user=user).first()
                    profile = ProfileModel.objects.filter(user=user).first()
                    profileimage = profileImage.objects.filter(user=user).first()
                    # print(profile.roll_number)
                    reg = profile.roll_number + 234

                    context = {"applyInfo":applyInfo, "profile":profile, "profileimage":profileimage, "reg":reg}

                    return render(request, 'admitCart.html', context)
                else:
                    return render(request, 'student_toggle_dashboard.html', context={"massege":"You didn't Pay Free! Try Next Admission."})
            return render(request, 'student_toggle_dashboard.html', context={"massege":"You didn't Completed Admission Apply Proccess"})
            
        return render(request, 'student_toggle_dashboard.html', context={"massege":"You are not valid informations!"})



class admitcartDate(View):
    
    def post(self, request, *args, **kwargs):
        unit = request.POST.get('unit')
        
        dates, created = publishDate.objects.get_or_create(
            unit=unit
        )
        
        dates.unit = unit
        dates.admitcart = True

        dates.save()
        return render(request, 'teacher_toggle_dashboard.html', context={"message":"Successfully Publish Admit Cart!"})


class Result(View):
    def post(self, request, *args, **kwargs):
        # unit = None
        
        unit = request.POST.get('unit')

        # print(unit, "==========================")

        # Fetch the first publishDate object matching the unit
        dates = publishDate.objects.filter(unit=unit).first()

        if dates:
            # Update the fields that are provided in the request
            dates.result = True  # Set the result field to True

            # Save the updated object
            dates.save()

            message = "Successfully Published Result!"
        else:
            message = "Unit not found!"

        return render(request, 'teacher_toggle_dashboard.html', context={"message": message})



# show result

class ResultView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'showresultform.html')
    
    def post(self, request, *args, **kwargs):
        unit = request.POST.get('unit')
        try:
            dated = publishDate.objects.get(unit=unit)
            if dated.result:
                results = ResultSheet.objects.filter(unit=unit).order_by('-obtain_mark')
                rank = None
                obtain_mark = None

                rolluser = ProfileModel.objects.get(user=request.user)
                roll = rolluser.roll_number

                for index, result in enumerate(results):
                    if result.roll == int(roll):
                        rank = index + 1
                        obtain_mark = result.obtain_mark
                        break
                
                print(rank, obtain_mark)

                if rank is not None:
                    context = {

                        'results': results,
                        'student_rank': rank,
                        'obtain_mark': obtain_mark,
                    }
                return render(request, 'showresult.html', context)
            else:
                return render(request, 'student_toggle_dashboard.html', context={"message": "Result does not publish yet!"})
        except publishDate.DoesNotExist:
            return render(request, 'student_toggle_dashboard.html', context={"message": "Unit not found!"})





class PublishMeritPosition(View):
    def post(self, request, *args, **kwargs):
        unit = request.POST.get('unit')
        first = request.POST.get('first')
        second = request.POST.get('second')
        instance = MeritPosition.objects.create(unit=unit, first=first, second=second)
        num = instance.number
        context = {
            "message": f"{unit} Unit {num} No Merit List Published!"
        }
        return render(request, 'teacher_toggle_dashboard.html', context)
        
        





    