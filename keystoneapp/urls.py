from django.urls import path
from .views import Index, Admission, AddStudent, Success, Login, Dashboard, Error404



urlpatterns = [
    path('', Index, name='index' ),
    path('admission/', Admission, name="admission"),
    path('addStudent/', AddStudent, name="addStudent"),
    path('success/', Success, name="success"),
    path('login/', Login, name="login"),
    path('dashboard/', Dashboard, name="dashboard"),
    path('error404/', Error404, name="error404"),





]
