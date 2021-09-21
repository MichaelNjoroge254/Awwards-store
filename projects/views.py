from __future__ import unicode_literals

from django.shortcuts import render
from django.http  import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Profile,Project,User,Post
from .forms import UserUpdateForm,ProfileUpdateForm,ProjectsForm
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import ProfileSerializer,ProjectSerializer

# Create your views here.
class ProfileList(APIView):
    def get (self,request):
        profile = Profile.objects.all()
        serializer = ProfileSerializer(profile,many=True)
        return Response(serializer.data)

    def post(self):
        pass

class ProjectList(APIView):
    def get(self,request):
        project = Project.objects.all()
        serializer=ProjectSerializer(project,many=True)
        return Response(serializer.data)

    def post(self):
        pass

def landing(request):
    return render(request,'landing.html')

@login_required(login_url='/accounts/login/')
def projects(request):
    project = Project.objects.all()
    return render(request,'projects.html',{"project":project})

def register(request):
    return render(request,'registration/register_form.html')

@login_required(login_url='/accounts/login/')
def postprojects(request):
    projform = ProjectsForm()
    projform.owner = request.user
    if request.method == "POST":
        projform = ProjectsForm(request.POST,request.FILES)
        if projform.is_valid():
           projform.save()
           return render (request,'projects.html')
        else:
           projform=ProjectsForm(request.POST,request.FILES)

    return render(request,'projects_form.html',{"projform":projform})

@login_required(login_url='/accounts/login/')
def profile(request):
    profile=Profile.objects.all()
    user = request.user
    project = Project.objects.filter(user=user)
    return render(request,'profile.html',{"profile":profile,"project":project})

@login_required(login_url='/accounts/login/')
def editdp(request):
    p_form = ProfileUpdateForm(request.POST,request.FILES)
    if request.method == 'POST':
        p_form = ProfileUpdateForm(request.POST,request.FILES)
        if p_form.is_valid():
            add = p_form.save(commit=False)
            add.save()
            return render(request,'profile.html')
        else:
            p_form = ProfileUpdateForm(request.POST,request.FILES)

    return render(request,'edit.html',locals())