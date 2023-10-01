from django.urls import path
from .views import HomePageView, AboutPageView, ContactPageView, ResumePageView

urlpatterns = [
    path("resume/", ResumePageView.as_view(), name='resume'),
    path("contact/", ContactPageView.as_view(), name='contact'),
    path("about/", AboutPageView.as_view(), name='about'),
    path("", HomePageView.as_view(), name='home'),
]
