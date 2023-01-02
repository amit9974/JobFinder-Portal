from django import forms
from django.contrib.auth.models import User
from .models import Job_Post, Job_Category, CandidateProfile, Job_Apply
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm



class CandidateRegisterForm(forms.Form):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    username = forms.CharField(max_length=10)
    email = forms.EmailField()
    password1 = forms.CharField(max_length=10, widget=forms.PasswordInput(),label='Create Password')
    password2 = forms.CharField(max_length=10, widget=forms.PasswordInput(),label='Confirm Password')
    


    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username__iexact=username)
        if qs.exists():
            raise forms.ValidationError('Username is already exists.')
        return username

    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email__iexact=email)
        if qs.exists():
            raise forms.ValidationError('Email is already exists.')
        return email



class LoginForm(forms.Form):
    username = forms.CharField(max_length=100,widget=forms.TextInput())
    password = forms.CharField(max_length=20, widget=forms.PasswordInput())

    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username__iexact=username)
        if not qs.exists():
            raise forms.ValidationError('Username is not exists')
        return username
        

class CompanyRegistrationForm(forms.Form):
    first_name = forms.CharField(max_length=200,widget=forms.TextInput(),label='Company Name')
    username = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)
    password1 = forms.CharField(max_length=10,widget=forms.PasswordInput(),label='New Password')
    password2 = forms.CharField(max_length=10,widget=forms.PasswordInput(),label='Confirm Password')
    is_staff = forms.BooleanField(required=True, widget=forms.CheckboxInput(),label='Company')

    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username__iexact=username)
        if qs.exists():
            raise forms.ValidationError('username is exists')
        return username
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email__iexact=email)
        if qs.exists():
            raise forms.ValidationError('Email is already exists.')
        return email



class JobPostForm(ModelForm):
    class Meta:
        model = Job_Post
        fields = [
            'profile', 'salary','experience','location','roles_responsibilities','about_company','contact','pincode'
        ]
        

class UpdateJobForm(forms.ModelForm):
    class Meta:
        model = Job_Post
        fields = ('profile','salary','experience','location','roles_responsibilities','about_company','contact','pincode')


class CandidateProfileForm(forms.ModelForm):
    class Meta:
        model = CandidateProfile
        fields = ('company_name','experience','current_ctc','location','mobile','resume')
        
        

class JobApplyForm(forms.ModelForm):
    class Meta:
        model = Job_Apply
        fields = [
            'name', 'email', 'mobile', 'post_for_apply', 'message'
        ]

        widgets ={'name':forms.TextInput(),
                'email':forms.EmailInput(),
                'mobile':forms.IntegerField(),
                'post_for_apply':forms.TextInput(),
                'message':forms.TextInput(),
                }
