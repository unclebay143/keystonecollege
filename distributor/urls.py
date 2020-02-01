from django.urls import path
from .views import Science, Art, Commercial, Contact

urlpatterns = [
path('science/', Science, name="science"),
path('art/', Art, name="art"),
path('commercial/', Commercial, name="commercial"),
path('contact/', Contact, name="contact"),

]
