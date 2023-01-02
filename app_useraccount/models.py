from django.db import models
from django.contrib.auth.models import User


class Job_Category(models.Model):
    name = models.CharField(max_length=100)
    img = models.FileField(upload_to='media/job_category/icon', null=True, blank=True)
    def __str__(self) -> str:
        return self.name 


class Job_Post(models.Model):
    img = models.FileField(upload_to='media/job_profile_pic/', null=True, blank=True)
    category = models.ForeignKey(Job_Category,on_delete=models.CASCADE,null=True)
    jobholder = models.ForeignKey(User,on_delete=models.CASCADE, default=None, null=True)
    profile = models.CharField(max_length=100)
    salary = models.CharField(max_length=10,null=True)
    experience = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    roles_responsibilities = models.TextField(max_length=500)
    about_company = models.CharField(max_length=200)
    contact = models.CharField(max_length=150)
    pincode = models.PositiveIntegerField()
    posted_at = models.DateField(auto_now=True, null=True)
    job_type = models.CharField(max_length=20, null=True)
    

    def __str__(self):
        return self.profile


class CandidateProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    profile_name = models.CharField(max_length=100, null=True)
    company_name = models.CharField(max_length=100)
    experience = models.CharField(max_length=20)
    current_ctc = models.CharField(max_length=20)
    expected_ctc = models.CharField(max_length=20, null=True)
    location = models.CharField(max_length=100)
    mobile = models.CharField(max_length=10)
    resume = models.FileField(upload_to='media/employee/resume')
    about_me = models.TextField(max_length=1000, null=True)
    preferred_location = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.user.first_name



class Job_Apply(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    mobile = models.PositiveIntegerField()
    post_for_apply = models.CharField(max_length=100)
    message = models.CharField(max_length=300)

    def __str__(self):
        return self.name

        