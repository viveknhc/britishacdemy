# Create web/urls.py and paste the following
from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = 'web'

urlpatterns = [
    path('', views.index,name="index"),
    path('about/', views.about,name="about"),
    path('contact/', views.contact,name="contact"),
    path('events/', views.events,name="events"),

    path('updates/', views.updates,name="updates"),
    path('update_details/<str:slug>/', views.update_details,name="update_details"),

    path('courses-category/', views.courses_category,name="courses_category"),
    path('courses/<str:slug>/', views.courses,name="courses"),
    path('course-details/<str:slug>/', views.course_details,name="course_details"),
    
]