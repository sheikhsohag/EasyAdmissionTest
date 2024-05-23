from django.contrib import admin
from .models import ApplicatinCondition,Prospectus, ResultSheet, GotSubject, Admitcard, Transactions, Notices, ApplyInformation, publishDate

# Register your models here.

class ApplicationAdmin(admin.ModelAdmin):
    list_display = ['UnitName', 'user']
admin.site.register(ApplicatinCondition, ApplicationAdmin)

class ProspectusAdmin(admin.ModelAdmin):
    list_display = ('user', 'unit', 'pdf_file', 'uploaded_at')

class ResultSheetAdmin(admin.ModelAdmin):
    list_display = ('unit', 'obtain_mark', 'roll')

class GotSubjectAdmin(admin.ModelAdmin):
    list_display = ('unit', 'subject', 'roll', 'gender')


class AdmitCardAdmin(admin.ModelAdmin):
    list_display = ('user', 'roll')

class TransactionsAdmin(admin.ModelAdmin):
    list_display = ('user', 'transection_id')

class NoticesAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'unit', 'title', 'notice')

admin.site.register(Notices, NoticesAdmin)


class ApplyInformationAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'unit')

admin.site.register(ApplyInformation, ApplyInformationAdmin)

class publishDateAdmin(admin.ModelAdmin):
    list_display = ('id', 'admitcart', 'result')

admin.site.register(publishDate, publishDateAdmin)


admin.site.register(Prospectus, ProspectusAdmin)
admin.site.register(ResultSheet, ResultSheetAdmin)
admin.site.register(GotSubject, GotSubjectAdmin)
admin.site.register(Admitcard, AdmitCardAdmin)
admin.site.register(Transactions, TransactionsAdmin)
