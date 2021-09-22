from django.urls import path,include
from .views import home_page,signup_view,post_project,project_view, search_results,profile,update_profile,user_profile
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views  as auth_views


app_name ="main"


urlpatterns=[
 
path('',home_page,name='home'),
path('signup/', signup_view, name='signup'),
path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
path('logout/', auth_views.LogoutView.as_view(next_page = '/')),

path('post_project/', post_project,name="post_project"),
path('project_view/<int:id>', project_view,name="project_view"),
path('search/',search_results, name='search_results'),

path('user_profile/<str:username>',user_profile, name='user_profile'),
path('profile/<str:username>',profile, name='profile'),
path('update_profile/<str:username>',update_profile, name='update_profile'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root= settings.MEDIA_ROOT)