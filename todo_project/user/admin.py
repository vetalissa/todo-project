from django.contrib import admin

from todo.models import Todo


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'status')
    fields = ('title', 'description', ('status', 'date_create', 'user'))
    readonly_fields = ('date_create', 'user')
