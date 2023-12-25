from django.urls import path

from django.contrib.auth.views import LogoutView

from user.views import UserRegisterView, UserLoginView

app_name = 'user'

urlpatterns = [
    path('registration/', UserRegisterView.as_view(), name='registration'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
