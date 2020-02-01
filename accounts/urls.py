from django.urls import path
from .views import Dashboard, Staff, Student


urlpatterns = [
    path('dashboard/', Dashboard, name="dashboard"),
    path('staff/', Staff, name="staff"),
    path('student/', Student, name="student"),





]
