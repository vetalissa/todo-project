from django.urls import path

from todo.views import (TodoCompletedListView, TodoCreateView, TodoListView,
                        TodoUpdateView, todo_deleted, todo_update_status)

app_name = 'todo'

urlpatterns = [
    path('create/', TodoCreateView.as_view(), name='create_todo'),
    path('todo-list/', TodoListView.as_view(), name='list_todo'),
    path('todo-ready/', TodoCompletedListView.as_view(), name='list_ready'),
    path('todo-update/<int:pk>', TodoUpdateView.as_view(), name='update_todo'),
    path('todo-status/<int:todo_id>/', todo_update_status, name='status_todo'),
    path('todo-deleted/<int:todo_id>/', todo_deleted, name='deleted_todo'),
]
