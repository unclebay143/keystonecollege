from django.urls import path
from .views import Index, Admission, AddStudent, Success, Error404,Login



urlpatterns = [
    path('', Index, name='index' ),
    path('admission/', Admission, name="admission"),
    path('addStudent/', AddStudent, name="addStudent"),
    path('success/', Success, name="success"),
    path('error404/', Error404, name="error404"),
    path('login/', Login, name="login"),





]
