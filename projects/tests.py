from __future__ import unicode_literals

from django.test import TestCase
from .models import Project,Profile
from django.contrib.auth.models import User

# Create your tests here.

# Create your models here.
class ProfileTestClass(TestCase):
    def setUp(self):
        self.new_user = User.objects.create_user(username='user',password='testpassword')
        self.new_profile = Profile(user=self.new_user,dpicture='jessica-felicio-1106325-unsplash.jpg',bio='user-bio')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_profile,Profile))

    def test_save_profile(self):
        self.new_profile.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)

    def test_delete_profile(self):
        self.new_profile.delete_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles)== 0)

    def test_update_bio(self):
        self.new_profile.save_profile()
        self.new_profile = Profile.objects.get(id=1)
        profile = self.new_profile
        profile.update_bio('updated user-bio')
        self.updated_profile = Profile.objects.get(id=1)
        self.assertEqual(self.updated_profile.bio,'updated user-bio')

class ProjectTestClass(TestCase):
    def setUp(self):
        self.new_user = User.objects.create_user(username='user', password='password')
        self.new_profile = Profile(user=self.new_user)
        self.new_profile.save()
        self.new_project = Project(id=1, project_image='pic.jpeg', title='Test Project',description='Test Description', owner=self.new_user, link='http://livesite.com')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_profile, Profile))

    def test_save_project(self):
        self.new_project.save_project()
        projects = Project.objects.all()
        self.assertTrue(len(projects) > 0)

    def test_delete_project(self):
        self.new_project.delete_project()
        projects = Project.objects.all()
        self.assertTrue(len(projects) == 0)