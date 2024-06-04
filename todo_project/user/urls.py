from django.contrib.auth.views import LogoutView
from django.urls import path

from user.views import UserLoginView, UserRegisterView

app_name = 'user'

urlpatterns = [
    path('registration/', UserRegisterView.as_view(), name='registration'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
