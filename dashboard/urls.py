from django.urls import path
from api.views import AllUsers,delete_user,update_user

urlpatterns = [
    path('users/',AllUsers,name='users')
]
