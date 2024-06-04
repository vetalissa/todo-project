from django.contrib import admin
from django.contrib.auth.models import User

from todo.admin import TodoLineAdmin

admin.site.unregister(User)


@admin.register(User)
class TodoUserAdmin(admin.ModelAdmin):
    list_display = ('username',)
    inlines = (TodoLineAdmin,)
