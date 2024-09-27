from . import views
from django.urls import path

app_name = "home_app"
urlpatterns = [
    path("", views.home_page, name="main"),
    path("send_email", views.send_email, name="send_email"),
    path("email_sent_successfully", views.email_sent_successfully, name="email_sent_successfully"),
]
