from django.shortcuts import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView

from common.views import TitleMixin
from todo.forms import TodoForm
from todo.models import Todo


class TodoCreateView(TitleMixin, CreateView):
    model = Todo
    form_class = TodoForm
    title = 'Новая задача'
    template_name = 'todo/create.html'
    success_url = reverse_lazy('todo:list_todo')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TodoCreateView, self).form_valid(form)


class TodoList(TitleMixin, ListView):
    model = Todo
    template_name = 'todo/list_todo.html'
    title = 'Список задач'
    queryset = Todo.objects.all()
    ordering = ('-date_create',)


class TodoListView(TodoList):
    title = 'Список задач'

    def get_queryset(self):
        queryset = super(TodoListView, self).get_queryset()
        return queryset.filter(user=self.request.user, status=0)


class TodoCompletedListView(TodoList):
    title = 'Завершенные задачи'

    def get_queryset(self):
        queryset = super(TodoCompletedListView, self).get_queryset()
        return queryset.filter(user=self.request.user, status=1)


class TodoUpdateView(UpdateView):
    template_name = 'todo/update_todo.html'
    model = Todo
    form_class = TodoForm
    success_url = reverse_lazy('todo:list_todo')

    def get_context_data(self, **kwargs):
        context = super(TodoUpdateView, self).get_context_data()
        context['title'] = self.object.title
        context['todo'] = self.object
        return context


def todo_deleted(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.delete()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])


def todo_update_status(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    if todo.status == 1:
        todo.status = 0
    else:
        todo.status = 1
    todo.save()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])
