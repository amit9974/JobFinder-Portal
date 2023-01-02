from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import *
from .models import *
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.

#=========================HOMEPAGE=========================
def HomePage(request):
    jobs = Job_Post.objects.all()[:10]
    cat = Job_Category.objects.all()[:8]
    ctx = {
        'cat':cat,
        'title':'Home Page',
        'jobs':jobs,
    }
    return render(request, 'index.html', ctx)


#=========================GET ALL JOB CATEGORIES=========================
@login_required(login_url='login')
def all_job_category(request):
    job = Job_Post.objects.all()
    ctx = {
        'job':job
    }
    return render(request, 'job/all_job_category.html', ctx)


#=========================FIND JOB PAGE=========================
def find_job(request):
    job = Job_Post.objects.all()
    cat = Job_Category.objects.all()[:12]
    page_num = request.GET.get('page', 1)
    paginator = Paginator(job, 6)
    try:
        page_obj = paginator.page(page_num)
    except PageNotAnInteger:
        # if page is not an integer, deliver the first page
        page_obj = paginator.page(1)  
    except EmptyPage:
        # if the page is out of range, deliver the last page
        page_obj = paginator.page(paginator.num_pages)  
    ctx={
        'cat':cat,
        'page_obj':page_obj,
    }
    return render(request, 'job/find_job.html', ctx)


#=========================JOB DEATAILS PAGE=========================
@login_required(login_url='login')
def job_details_page(request, id):
    job = Job_Post.objects.get(id=id)
    cat = Job_Category.objects.all()
    ctx = {
        'job':job,
        'cat':cat,
    }
    return render(request, 'job/job_details.html', ctx)


#=========================SEARCH JOB=========================
def search_job(request):
    ctx ={}
    query = request.GET.get('q')
    job = Job_Post.objects.filter(profile__icontains = query)
    ctx ={
        'q':query,
        'job':job,
    }
    return render(request, 'job/search_job.html', ctx)