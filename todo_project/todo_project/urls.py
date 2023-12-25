from django.contrib import admin
from django.urls import path, include

from home.views import HomeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('user/', include('user.urls', namespace='user')),
    path('todo/', include('todo.urls', namespace='todo')),
]
