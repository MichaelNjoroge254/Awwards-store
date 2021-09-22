from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Project,Profile,Rating

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254)
    fullname=forms.CharField(max_length=254)

    class Meta:
        model = User
        fields = ('username', 'fullname', 'email', 'password1','password2')


class SubmitProjectForm(forms.ModelForm):
    technologies=forms.CharField(label='technologies',widget=forms.TextInput(attrs={'placeholder': 'technologies separate with ,'}))
                                
    class Meta:
        model = Project
        fields = ('name','project_image', 'description','link','technologies')
        
class RateForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields=['design','content','usability'] 
        
        
class UpdateUserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio', 'profile_picture','location','facebook_link','twitter_link','github_link')