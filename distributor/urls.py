from django.urls import path
from .views import Science, Art, Commercial, Contact, About

urlpatterns = [
path('science/', Science, name="science"),
path('art/', Art, name="art"),
path('commercial/', Commercial, name="commercial"),
path('contact/', Contact, name="contact"),
path('about/', About, name="about"),


]
