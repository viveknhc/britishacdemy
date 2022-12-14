
from django.db import models
from versatileimagefield.fields import VersatileImageField
from tinymce.models import HTMLField
from django.urls import reverse
from django.template.defaultfilters import slugify

class Banner(models.Model):
    image = VersatileImageField(upload_to = 'Banner/')
    sub_heading = models.CharField(max_length=100)
    main_heading = models.CharField(max_length=350)
    short_description = models.CharField(max_length=350)

class Testimonial(models.Model):
    name         = models. CharField(max_length = 350)
    description  = models.CharField(max_length = 350)
    designation  = models.CharField(max_length = 350)
    image        = VersatileImageField(upload_to ='testimonial/')

    def __str__(self):
        return str(self.name)


class Update(models.Model):
    title        = models.CharField(max_length = 350)
    summary      = models.CharField(max_length = 555)
    content      = HTMLField(blank = True, null = True)
    image        = VersatileImageField(upload_to = 'Blogs/')
    date         = models.DateField()
    slug         = models.SlugField(unique=True) 

    def get_absolute_url(self):
        return reverse('web:update_details', kwargs={'slug': self.slug})

    def __str__(self):
        return str(self.title)


class Event(models.Model):
    title = models.CharField(max_length=128)
    description  = models.CharField(max_length = 350)
    date =models.DateField()
    image =VersatileImageField(upload_to ="events/")
    time = models.TimeField()

    def __str__(self):
        return str(self.title)


class Feedback(models.Model):
    name = models.CharField(max_length=128)
    email = models.EmailField()
    message  =models.TextField()

    def __str__(self):
        return str(self.name)


class Category(models.Model):
    title = models.CharField(max_length=128)
    icon        = VersatileImageField(upload_to = 'category/')
    slug = models.SlugField(unique=True)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        verbose_name_plural= ('Course Categories')

    def __str__(self):
        return str(self.title)


class Course(models.Model):
    CERTIFICATE_CHOICES =(('yes','yes'),('No','No'))
    category  =models.ForeignKey(Category,on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    summary = models.CharField(max_length=250)
    image = VersatileImageField(upload_to="courses/")
    content = HTMLField(blank=True,null=True)
    students = models.IntegerField()
    lessons = models.IntegerField()
    length = models.CharField(max_length=128)
    effort = models.CharField(max_length=128)
    institution =models.CharField(max_length=128)
    subject = models.CharField(max_length=128)
    language = models.CharField(max_length=128)
    certificate = models.CharField(max_length=128,choices=CERTIFICATE_CHOICES)
    price = models.CharField(max_length=8)
    slug = models.SlugField(unique=True)
    is_active = models.BooleanField(default=True)


    def __str__(self):
        return str(self.title)


class Instructor(models.Model):
    name         = models. CharField(max_length = 350)
    subject      = models.ForeignKey(Course,on_delete=models.CASCADE)
    image        = VersatileImageField(upload_to ='instructor/')

    def __str__(self):
        return str(self.name)


class Contact(models.Model):
    name  = models.CharField(max_length = 128)
    email       = models.EmailField(blank = True, null = True)
    phone       = models.CharField(max_length = 15)
    subject     = models.CharField(max_length = 128)
    message     = models.TextField()

    def __str__(self):
        return str(self.name)

class Subscriber(models.Model):
    email       = models.EmailField()

    def __str__(self):
        return str(self.name)