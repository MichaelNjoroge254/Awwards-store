from django.test import TestCase
from django.contrib.auth.models import User
from .models import Project,Rating,Profile


class RatingTestClass(TestCase):
    def setUp(self):
        self.user = User(id=1,username='Michael')
        self.user.save()
        self.user_profile = Profile(user=self.user,profile_picture="good_picture.png",bio="My bio")
        self.new_project = Project(id=1,name="AwsomeApp",project_image="image.png",description="Awsome project",user=self.user_profile )
        self.new_project.save()
        self.project_rating = Rating(id=1,design=7,usability=8,content=9,user=self.user_profile,project=self.new_project)
   
    def tearDown(self):
        User.objects.all().delete()
        Profile.objects.all().delete()
        Project.objects.all().delete()
        
    def test_instance(self):
        self.assertTrue(isinstance(self.project_rating,Rating))
    
    def test_save_rating(self):
        self.project_rating.save_rating()
        ratings=Rating.objects.all()
        self.assertTrue(len(ratings)>0)
        
    def test_delete_rating(self):
        self.project_rating.save_rating()
        self.project_rating.delete_rating()
        ratings=Rating.objects.all()
        self.assertTrue(len(ratings)==0)
        
    def test_get_project_rating(self):
        id=1
        self.project_rating.get_project_rating(id)
        self.assertEquals(self.project_rating.id,1)
        
        

class ProjectTestClass(TestCase):
    def setUp(self):
        self.user = User(id=1,username='Michael')
        self.user.save()
        self.user_profile = Profile(user=self.user,profile_picture="good_picture.png",bio="My bio")
        self.new_project = Project(name="AwsomeApp",project_image="image.png",description="Awsome project",user=self.user_profile )
   
    def tearDown(self):
        User.objects.all().delete()
        Project.objects.all().delete()
        
    def test_instance(self):
        self.assertTrue(isinstance(self.new_project,Project))
    
    def test_save_project(self):
        self.new_project.save_project()
        projects=Project.objects.all()
        self.assertTrue(len(projects)>0)
        
    def test_delete_project(self):
        self.new_project.save_project()
        self.new_project.delete_project()
        projects=Project.objects.all()
        self.assertTrue(len(projects)==0)
       
        
    def test_get_project_by_id(self):
        id = 1
        self.new_project.save_project()
        self.new_project.get_project_by_id(id)
        self.assertEquals(self.new_project.name,'AwsomeApp')
        
    def test_search_project_by_search_term(self):
        search_term = 'Aws'
        self.new_project.save_project()
        project = Project.search_project_by_search_term(search_term)
        self.assertTrue(len(project)>0)
  
    

class ProfileTestClass(TestCase):
    #setup method
    def setUp(self):
        self.user = User(username='Michael')
        self.user.save()
        self.user_profile = Profile(user=self.user,profile_picture="good_picture.png",bio="My bio")
   
    def tearDown(self):
        User.objects.all().delete()
        Profile.objects.all().delete()
      
    def test_instance(self):
        self.assertTrue(isinstance(self.user_profile,Profile))
            
    def test_save_user_profile(self):
        self.user_profile.save_profile()
        profiles=Profile.objects.all()
        self.assertTrue(len(profiles)>0)
        
    def test_delete_user_profile(self):
        self.user_profile.save_profile()
        self.user_profile.delete_profile()
        profiles=Profile.objects.all()
        self.assertTrue(len(profiles)==0)
        
    def test_filter_profile_by_id(self):
        id=1
        self.user_profile.filter_profile_by_id(id)
        self.assertEquals(self.user_profile.user.username,'Michael')