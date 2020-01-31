from django.urls import path
from .views import Dashboard,Login



urlpatterns = [
    path('dashboard/', Dashboard, name="dashboard"),
    path('login/', Login, name="login"),


]
