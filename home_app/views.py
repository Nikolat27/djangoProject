import redis
from django.shortcuts import render, redirect
from .tasks import send_async_email
from django.core.cache import cache
from deployDjango import settings

# Create your views here.

redis_client = redis.Redis(host="127.0.0.1", port=6379, db=0)


# Celery worker run: celery -A deployDjango worker --loglevel=info

def home_page(request):
    return render(request, "home_app/index.html")


def send_email(request):
    if request.method == "POST":
        data = request.POST
        email = data.get("email")
        subject = data.get("subject")
        message = data.get("message")

        redis_client.set("last_email", email, ex=60 * 2)  # This caches just last 2 minutes
        redis_client.set("last_email_subject", subject, ex=60 * 2)
        redis_client.set("last_email_message", message, ex=60 * 2)
        send_async_email(subject=subject, email=email, message=message)
        return redirect("home_app:email_sent_successfully")

    return render(request, "home_app/send_email.html")


def email_sent_successfully(request):
    # Retrieve the last email subject and message from Redis
    email = redis_client.get("last_email")
    subject = redis_client.get("last_email_subject")
    message = redis_client.get("last_email_message")

    email = email.decode('utf-8') if email else 'No email sent or it`s expired'
    subject = subject.decode('utf-8') if subject else 'No subject sent or it`s expired'
    message = message.decode('utf-8') if message else 'No message sent or it`s expired'

    context = {
        "email": email,
        'subject': subject,
        'message': message,
    }

    return render(request, "home_app/email_sent_successfully.html", context)
