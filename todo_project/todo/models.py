from django.db import models

from django.contrib.auth.models import User


class Todo(models.Model):
    NOT_READY = 0
    READY = 1
    STATUSES = (
        (NOT_READY, 'Не выполнено'),
        (READY, 'Выполненно'),
    )

    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    important = models.BooleanField(default=False)
    date_create = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    status = models.PositiveSmallIntegerField(default=NOT_READY, choices=STATUSES)
