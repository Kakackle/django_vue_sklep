from django.db import models
from django.utils.text import slugify
from django.conf import settings
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from django.urls import reverse

from django.contrib import admin

# Create your models here.
class Subscriber(models.Model):
    WEEK = 7
    TWOWEEKS = 14
    MONTH = 31
    FREQUENCY_OPTIONS = (
        (WEEK,'weekly'),
        (TWOWEEKS, 'bi-weekly'),
        (MONTH, 'monthly')
    )
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    frequency = models.IntegerField(choices=FREQUENCY_OPTIONS, default=WEEK)
    conf_num = models.CharField(max_length=15,null=True, blank=True)
    confirmed = models.BooleanField(default=False)
    slug = models.SlugField(unique=True, default="temp")

    def __str__(self):
        return self.email + " (" + ("not " if not self.confirmed else "") + "confirmed)"
    
    def save(self, *args, **kwargs):
        if self.slug == 'temp':
            self.slug = slugify(self.email)
        return super().save(*args, **kwargs)
    
class Newsletter(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    subject = models.CharField(max_length=150)
    contents = models.FileField(upload_to='mail_templates/newsletters/')

    def __str__(self):
        return self.subject + " " + self.created_at.strftime("%B %d, %Y")
    
    def send(self, request):
        contents = self.contents.read().decode('utf-8')
        subscribers = Subscriber.objects.filter(confirmed=True)
        sg = SendGridAPIClient(settings.SENDGRID_API_KEY)
        for sub in subscribers:
            message = Mail(
                    from_email=settings.FROM_EMAIL,
                    to_emails=sub.email,
                    subject=self.subject,
                    html_content=contents + (
                        '<br><a href="{}?email={}&conf_num={}">Unsubscribe</a>.').format(
                            request.build_absolute_uri(reverse('newsletter:newsletter_unsubscribe')),
                            sub.email,
                            sub.conf_num))
            sg.send(message)
        # for sub in subscribers:
        #     message = Mail(
        #             from_email=settings.FROM_EMAIL,
        #             to_emails=sub.email,
        #             subject=self.subject,
        #             html_content=contents + (
        #                 '<br><a href="{}>Unsubscribe</a>.').format(
        #                     request.build_absolute_uri(reverse('api:subscribers', kwargs={'slug': sub.slug})),))
        #     sg.send(message)

class NewsletterAdmin(admin.ModelAdmin):
    # actions = [send_newsletter]
    list_display = ('created_at', 'updated_at', 'subject', 'contents', 'send')    