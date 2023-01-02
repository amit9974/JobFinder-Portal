from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import *
from .models import *
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required




#=========================COMPANY DASHBOARD=========================
@staff_member_required
def Company_Dashboard(request):
    job = Job_Post.objects.filter(jobholder=request.user)
    return render(request, 'company/company_dashboard.html',{'job':job})


def Company_Profile_Page(request):
    comp = User.objects.get(id = request.user.id)
    ctx={
        'comp':comp
    }
    return render(request, 'profile/company_profile.html', ctx)

#=========================CREATE NEW JOB POST BY COMPNAY=========================
@staff_member_required
def create_job(request,id):
    cat = Job_Category.objects.all()
    job = Job_Post.objects.filter(jobholder=id)
    if request.method == "POST":
        form = JobPostForm(request.POST or None)
        if form.is_valid():
            form.save(commit=False).jobholder = request.user
            form.save()
            return redirect('company_dashboard')
        else:
            messages.error(request, ('Invalid Form'))
    else:
        return render(request, 'job/create_job.html',{'job':job,'cat':cat})
    


#=========================GET ALL JOB LIST=========================
@login_required(login_url='login')
def all_job_list(request):
    job = Job_Post.objects.filter(jobholder=request.user)
    
    ctx = {
        'job':job,
    }
    return render(request,'job/all_job.html', ctx)


#===========================FIND EMPLOYEE ===========================
def find_employee(request):
    cand = CandidateProfile.objects.all()
    ctx ={
        'cand':cand
    }
    return render(request, 'employees/find_employee.html',ctx)



def employee_details(request, id):
    emp = CandidateProfile.objects.get(id=id)
    ctx={
        'emp':emp,
    }
    return render(request, 'employees/employee_details.html', ctx)

#=========================EDIT JOB PAGE=========================
@staff_member_required
def edit_job(request, id):
    job = Job_Post.objects.get(id=id)
    ctx = { 
        'job':job
    }
    return render(request, 'job/edit_job.html', ctx)

#=========================UPDATE JOB=========================
@staff_member_required
def updatejob(request, id):
    job = Job_Post.objects.get(id=id)
    form = UpdateJobForm(request.POST, instance=job)
    if form.is_valid():
        form.save()
        messages.success(request, ('Job details has been updated'))
        return redirect('all_job')
    else:
        messages.error(request, ("Something went wrong"))

    return render(request, 'job/edit_job.html')

#=========================DELETE JOB PAGE=========================
@staff_member_required
def delete_page(request, id):
    job = Job_Post.objects.get(id=id)
    ctx={
        'job':job
    }
    return render(request, 'job/delete_job.html', ctx)

#=========================DELETE THE JOB=========================
@staff_member_required
def delete_job(request, id):
    job = Job_Post.objects.get(id=id)
    job.delete()
    return redirect('all_job')

