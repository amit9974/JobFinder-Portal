from django.contrib import admin
from .models import Job_Post, Job_Category, CandidateProfile
# Register your models here.



@admin.register(Job_Post)
class Job_Admin(admin.ModelAdmin):
    '''Admin View for Job_'''

    list_display = ('profile','salary','experience','location','about_company')
    list_filter = ('profile','salary','experience','location')

admin.site.register(Job_Category)
admin.site.register(CandidateProfile)

