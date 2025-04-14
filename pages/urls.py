from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_view, name="home"),
    path("about-me/", views.about_view, name="about-me"),
    path("contact/", views.contact_view, name="contact")

]

