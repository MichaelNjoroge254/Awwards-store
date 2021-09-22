from django.db import models
from cloudinary.models import CloudinaryField  
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime as dt


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True)
    profile_picture = models.ImageField(upload_to = 'pictures/',default='pictures/user.png')
    bio = models.TextField(max_length=500, default="My Bio", blank=True)
    location = models.CharField(max_length=250, default="Hometown",blank=True)
    facebook_link=models.URLField(blank=True)
    github_link=models.URLField(blank=True)
    twitter_link=models.URLField(blank=True)
  
    def __str__(self):
        return f'{self.user} Profile'
        
    
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    def save_profile(self):
        self.user

    def delete_profile(self):
        self.delete()
    
    @classmethod
    def filter_profile_by_id(cls, id):
        profile = Profile.objects.filter(user__id = id).first()
        return profile

  


class Project(models.Model):
    name = models.CharField(max_length=250, blank=True)
    project_image = CloudinaryField('image')
    description = models.TextField(max_length=500, default="Project description", blank=True)
    link=models.URLField()
    technologies = models.CharField(max_length=200, blank=True)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='posts')
    posted_at = models.DateTimeField(auto_now_add=True, null=True)
    

    class Meta:
        ordering = ["-pk"]

    def save_project(self):
        self.save()

    def delete_project(self):
        self.delete()
    
    @classmethod
    def get_project_by_id(cls,id):
        project = Project.objects.filter(id=id)
        return project
    
    @classmethod
    def search_project_by_search_term(cls,search_term):
        return cls.objects.filter(name__icontains=search_term).all()

    def __str__(self):
        return f'{self.name} Project'
    
    
    
class Rating(models.Model):
    rating = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
        (9, '9'),
        (10, '10'),
    )

    design = models.IntegerField(choices=rating, default=0, blank=True)
    usability = models.IntegerField(choices=rating, blank=True)
    content = models.IntegerField(choices=rating, blank=True)
    score = models.FloatField(default=0, blank=True)
    design_average = models.FloatField(default=0, blank=True)
    usability_average = models.FloatField(default=0, blank=True)
    content_average = models.FloatField(default=0, blank=True)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, related_name='rater')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='ratings', null=True)
    rated_at=models.DateTimeField(auto_now_add=True)

    def save_rating(self):
        self.save()
    
    def delete_rating(self):
        self.delete()

    @classmethod
    def get_project_rating(cls, id):
        rating = Rating.objects.filter(project_id=id).all()
        return rating

    def __str__(self):
        return f'{self.project} Rating'
        