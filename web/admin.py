from django.contrib import admin
from . models import Testimonial,Category,Course,Update,Event,Feedback,Contact,Instructor,Subscriber,Banner
from django.contrib.auth.models import Group

admin.site.unregister(Group)

admin.site.register(Banner)

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
   pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
   prepopulated_fields = {'slug': ('title',)}


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
   prepopulated_fields = {'slug': ('title',)}



@admin.register(Update)
class UpdateAdmin(admin.ModelAdmin):
   prepopulated_fields = {'slug': ('title',)}


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
   pass

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
   pass

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
   pass

@admin.register(Instructor)
class InstructorAdmin(admin.ModelAdmin):
   pass