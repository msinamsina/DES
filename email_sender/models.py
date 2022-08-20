from django.contrib.auth.models import User
from django.db import models


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    sptm_server = models.CharField(max_length=100)
    sptm_port = models.CharField(max_length=100)
    sptm_user = models.CharField(max_length=100)
    sptm_password = models.CharField(max_length=100)
    credits = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username


class EmailSet(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    from_email = models.CharField(max_length=100)
    name = models.CharField(max_length=100, null=True, blank=True)
    subject = models.CharField(max_length=100, null=True, blank=True)
    body_html = models.FileField(upload_to='email_sender/static/email_sender/email_templates/', null=True, blank=True)
    contact_list = models.FileField(upload_to='email_sender/static/email_sender/email_contacts/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.customer.user.username + ' - (' + self.name + ')'


class Log(models.Model):
    email_set = models.ForeignKey(EmailSet, on_delete=models.CASCADE)
    sent_at = models.DateTimeField(auto_now_add=True)
    sent_to = models.CharField(max_length=100)
    sent_sataus_choices = (
        ('S', 'Sent'),
        ('F', 'Failed'),
        ('P', 'Pending'),
    )
    sent_status = models.CharField(max_length=100, choices=sent_sataus_choices, default='P')
    sent_message = models.CharField(max_length=100)

    def __str__(self):
        return self.customer.user.username + ' - (' + self.email_set.name + ')'
