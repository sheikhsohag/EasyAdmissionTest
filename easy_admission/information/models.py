from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ApplicatinCondition(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    UnitName = models.CharField(max_length=100)
    Taka = models.CharField(max_length=100)
    firstdate = models.DateField()
    lastdate = models.DateField()
    totalsit = models.CharField(max_length=100)
    sci_sit = models.CharField(max_length=100)  # Changed field name from 'Sci-sit' to 'Sci_sit'
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
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    unit = models.CharField(max_length=100)
    pdf_file = models.FileField(upload_to='pdfs/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.unit
class Notices(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    unit = models.CharField(max_length=10)
    notice = models.TextField(max_length=1000)
    uploaded_at = models.DateTimeField(auto_now_add=True)

class ResultSheet(models.Model):
    unit = models.CharField(max_length=100)
    obtain_mark = models.FloatField()
    roll = models.IntegerField()
    def __str__(self):
        return self.unit

class GotSubject(models.Model):
    unit = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    roll = models.IntegerField()

    def __str__(self):
        return self.subject

class Admitcard(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    roll = models.IntegerField()

class Transactions(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    transection_id = models.CharField(max_length=100)

    




