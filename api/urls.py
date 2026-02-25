from django.urls import path
from . import views


# endPoint http://localhost:8000/user/2
urlpatterns = [
    path('', views.HomePage, name='/'),
    path('user/<slug:title>', views.Dynamic, name="dynamic"),
    path('signup/', views.SignUp, name='register'),
    path('allusers/', views.AllUsers, name='users'),
    path('update/<int:name>', views.Update_Register_User, name='update')
]
