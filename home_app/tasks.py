from celery import shared_task
from django.core.mail import send_mail


@shared_task
def send_async_email(subject, message, email):
    send_mail(subject=subject, message=message, from_email='samalizadeh899@gmail.com', recipient_list=[email])
