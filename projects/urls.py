from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.landing, name='landing'),
    path('projects', views.projects, name='projects'),
    path('addproject',views.postprojects,name="postprojects"),
    path('profile', views.profile, name='profile'),
    path('editdp', views.editdp, name='editdp'),
    path('api/profile/',views.ProfileList.as_view()),
    path('api/project/',views.ProjectList.as_view())
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)