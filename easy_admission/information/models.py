from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ApplicatinCondition(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    UnitName = models.CharField(max_length=100)
    Taka = models.CharField(max_length=100)
    firstdate = models.DateField()
    lastdate = models.DateField()
    totalsit = models.CharField(max_length=100)
    sci_sit = models.CharField(max_length=100) 
    arts_sit = models.CharField(max_length=100)
    com_sit = models.CharField(max_length=100)
    tec_adu_sit = models.CharField(max_length=100)
    sci_qua = models.TextField()
    arts_qua = models.TextField()
    com_qua = models.TextField()
    tec_qua = models.TextField()


    def __str__(self):
        return self.UnitName
    
class Prospectus(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    unit = models.CharField(max_length=100)
    pdf_file = models.FileField(upload_to='pdfs/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.unit
class Notices(models.Model):
    title = models.CharField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    unit = models.CharField(max_length=10)
    notice = models.FileField(upload_to='pdfs/')
    uploaded_at = models.DateTimeField(auto_now_add=True)


class ResultSheet(models.Model):
    unit = models.CharField(max_length=100)
    obtain_mark = models.FloatField()
    roll = models.IntegerField()
    resultDate = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.unit

class GotSubject(models.Model):
    unit = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    roll = models.IntegerField()
    hall = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)

    def __str__(self):
        return self.subject

class Admitcard(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    roll = models.IntegerField()
    

class Transactions(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    transection_id = models.CharField(max_length=100)


class ApplyInformation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    unit = models.CharField(max_length=10)
    transactions = models.BooleanField(null=True, blank=True, default=False)
   

    def __str__(self):
        return f'Username {{self.user}} unit {{self.unit}}'
    


class publishDate(models.Model):
    admitcart = models.BooleanField(null=True, blank=True, default=False)
    result = models.BooleanField(null=True, blank=True, default=False)
    unit = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return f'admitcard {{self.admitcart}} unit {{self.result}}'
    

class MeritPosition(models.Model):
    unit = models.CharField(max_length=5)
    first = models.IntegerField()
    second = models.IntegerField()
    number = models.IntegerField(null=True, blank=True )
    exist = models.BooleanField(default=False)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'unit {self.unit} number of merit list {self.number}'
    
    def save(self, *args, **kwargs):
        max_number_instance = MeritPosition.objects.filter(unit=self.unit).order_by('-number').first()
        if max_number_instance:
            self.number = max_number_instance.number + 1
        else:
            self.number = 1
        super().save(*args, **kwargs)
