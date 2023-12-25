from django.urls import reverse_lazy
from django.contrib.auth import login

from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView

from common.views import TitleMixin


class UserRegisterView(TitleMixin, CreateView):
    title = 'Регистрация'
    template_name = 'user/registration.html'
    success_url = reverse_lazy('list_todo')
    form_class = UserCreationForm
    model = User

    def form_valid(self, form):
        valid = super(UserRegisterView, self).form_valid(form)
        login(self.request, self.object)
        return valid


class UserLoginView(TitleMixin, LoginView):
    title = 'Вход'
    template_name = 'user/login.html'
    form_class = AuthenticationForm
