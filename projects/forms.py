from django import forms
from .models import Profile,Project
from django.contrib.auth.models import User

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(max_length=250, help_text='Required. Inform a valid email address')

    class Meta:
            model = User
            fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields= ('user','dpicture','bio','projectsposted','contacts')

class ProjectsForm(forms.ModelForm):
    class Meta:
        model=Project
        fields = ['title','description','link','landingpic','user']