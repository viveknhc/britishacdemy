# Edit web/views.py
from unicodedata import category
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
import json
from . models import Testimonial, Category, Course, Update, Event, Instructor,Banner
from .forms import FeedbackForm, ContactForm, SubsriptionForm


def index(request):
    categories = Category.objects.filter(is_active=True)
    instructors = Instructor.objects.all()
    updates = Update.objects.all().order_by("-id")

    banner = Banner.objects.all().last()

    courses =Course.objects.all()
    form = FeedbackForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            data = form.save(commit=False)
            data.referral = "web"
            data.save()
            response_data = {
                "status" : "true",
                "title" : "Successfully Submitted",
                "message" : "Message successfully submitted"
            }
        else:
            print (form.errors)
            response_data = {
                "status" : "false",
                "title" : "Form validation error",
                "message" : repr(form.errors)
            }
        return HttpResponse(json.dumps(response_data), content_type='application/javascript')
    else:
        context = {
            "is_index": True,
            "instructors": instructors,
            "updates": updates,
            "form" : form,
            "categories": categories,
            "courses" : courses,
            "banner":banner
        }
        return render(request, 'web/index.html', context)


def about(request):
    testimonials = Testimonial.objects.all()
    context = {
        "is_about": True,
        "testimonials": testimonials,
    }
    return render(request, 'web/about.html', context)


def contact(request):
    form = ContactForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            data = form.save(commit=False)
            data.referral = "web"
            data.save()
            response_data = {
                "status" : "true",
                "title" : "Successfully Submitted",
                "message" : "Message successfully submitted"
            }
        else:
            print (form.errors)
            response_data = {
                "status" : "false",
                "title" : "Form validation error",
                "message" : repr(form.errors)
            }
        return HttpResponse(json.dumps(response_data), content_type='application/javascript')
    else:
        context = {
        "is_contact" : True,
        "form" : form,
        }
        return render(request,'web/contact.html',context)


def courses_category(request):
    categories = Category.objects.all()
    context = {
        "is_courses_category" : True,
        "categories" : categories,
    }
    return render(request, 'web/courses-category.html',context)


def courses(request,slug):
    courses =Course.objects.filter(category__slug=slug)
    courses_category = Category.objects.get(slug=slug)
    context = {
        "is_courses" : True,
        "courses" : courses,
        "courses_category" : courses_category,
    }
    return render(request, 'web/courses.html',context)


def course_details(request,slug):
    course = get_object_or_404(Course,slug=slug)
    courses = Course.objects.exclude(pk=course.pk) 

    context = {
        "is_course_details" : True,
        "course" : course,
        "courses" : courses,
    }
    return render(request, 'web/course-details.html',context)


def updates(request):
    updates = Update.objects.all().order_by("-id")
    context = {
        "is_updates" : True,
        "updates" : updates,
    }
    return render(request, 'web/updates.html',context)


def update_details(request,slug):
    update =get_object_or_404(Update,slug=slug)
    context = {
        "is_update_details" : True,
        "update" : update
    }
    return render(request, 'web/update-details.html',context)


def events(request):
    events = Event.objects.all().order_by("-id")
    context = {
        "is_events" : True,
        "events" : events
    }
    return render(request, 'web/events.html',context)



def handler404(request,exception):
    return render(request, 'error/404.html', status=404)