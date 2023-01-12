from django.conf import settings 
# html email required stuff

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from .models import FranchiseEnquire


def franchise_enquiry_mail(id):
    enquiry = FranchiseEnquire.objects.get(id=id)
    html_content = render_to_string("web/enquryemail.html",{'context':enquiry})
    text_content = strip_tags(html_content)
    subject = 'Franchise enquiry'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [settings.EMAIL_HOST_USER]
    email_obj = EmailMultiAlternatives(subject, text_content, email_from, recipient_list)
    email_obj.attach_alternative(html_content, "text/html")
    email_obj.send()