from django.views.generic.base import TemplateView

from common.views import TitleMixin


class HomeView(TitleMixin, TemplateView):
    template_name = 'home/home.html'
    title = 'Листок'
