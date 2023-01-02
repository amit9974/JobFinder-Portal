from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import JobApplyForm
from django.contrib import messages



#=========================CANDIDATE DASHBOARD=========================
def Candidate_Dashboard(request):
    return render(request, 'company/candidate_dashboard.html')


#============================ Candidate Profile =====================

def Candidate_Profile_Page(request):
   cand = CandidateProfile.objects.all()
   ctx={
    'cand':cand,
    }
   return render(request, 'profile/candidate_profile.html',ctx)

#==========================Update Candidate Profile ===================
def updateProfile(request, id):
    cand = CandidateProfile.objects.filter(id=id)
    ctx={
        'cand':cand,
    }
    return render(request, 'profile/update_cand_profile.html', ctx)




def Apply_For_Job(request):
    form = JobApplyForm(request.POST or None)
    if form.is_valid:
        form.save()
        messages(request, ('Applied Succesfully'))
        return redirect('all_job')
    else:
        messages.error(request,('Something went wrong'))
    ctx={
        'form':form
    }
    return render(request, 'job/job_details.html', ctx)