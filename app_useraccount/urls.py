from django.contrib import admin
from django.urls import path, include
from . import views, accounts, candidate, company
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    ############################ Project Views #####################################
    path('', views.HomePage, name='home'),
    path('job_details/<int:id>', views.job_details_page, name='job_details'),
    path('all_job_category/', views.all_job_category, name='all_job_category'),
    path('find_job/', views.find_job, name='find_job'),
    path('search/', views.search_job, name='search'),
    
    ############################## Account Views ###################################
    path('candidate_register/',accounts.CandidateRegisterPage, name='candidate_register'),
    path('company_register/', accounts.CompanyRegisterPage, name='company_register'),
    path('login/', accounts.LoginPage,name='login'),
    path('logout/', accounts.LogoutPage, name='logout'),

    ########################### Company Views ###################################    
    path('company_dashboard/', company.Company_Dashboard, name='company_dashboard'),
    path('company_profile/', company.Company_Profile_Page, name='company_profile'),
    path('create_job/<id>', company.create_job, name='create_job'),
    path('find_employee/', company.find_employee, name='find_employee'),
    path('all_job/', company.all_job_list, name='all_job'),
    path('edit_job/<int:id>', company.edit_job, name='edit_job'),
    path('update_job/<int:id>', company.updatejob, name='update_job'),
    path('delete/<int:id>', company.delete_page, name='delete'),
    path('delete_job/<int:id>', company.delete_job, name='delete_job'),
    path('employee_details/<int:id>', company.employee_details, name='employee_details'),
    
    ########################### Candidate Views ####################################
    path('candidate_dashboard/', candidate.Candidate_Dashboard, name='candidate_dashboard'),
    path('apply_job/', candidate.Apply_For_Job, name='apply_job'),
    path('candidate_profile/',candidate.Candidate_Profile_Page, name='candidate_profile'),
    path('update_candidate_profile/<int:id>', candidate.updateProfile, name='update_candidate_profile'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)