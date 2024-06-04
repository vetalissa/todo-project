from django.contrib import admin

from todo.models import Todo


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'status')
    fields = ('title', 'description', ('status', 'date_create', 'user'))
    readonly_fields = ('user', 'title', 'status', 'date_create', 'description')
    list_filter = ('user', 'status',)


class TodoLineAdmin(admin.TabularInline):
    model = Todo
    fields = ('title', 'status', 'date_create', 'description')
    readonly_fields = ('title', 'status', 'date_create', 'description')
    extra = 0
