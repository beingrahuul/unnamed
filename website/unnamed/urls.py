from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name='home'),
    path('login/', loginPage, name='login'),
    path('logout/', logoutUser, name='logout'),
    path('register/', registerPage, name='register'),
    path('user/', User, name='user'),
    path('complete_profile/', CompleteProfilePage, name='complete_profile'),
    path('change_name/', ChangeName, name='change_name'),

]
