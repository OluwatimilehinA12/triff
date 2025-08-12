from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("index", views.index, name="index"),
    path("otp_verification", views.otp_verification, name="otp_verification"),
    path("ads", views.ads, name="ads"),
    path("success", views.success, name="success"),
]