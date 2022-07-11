from django.urls import path

from todo.views import (
    TaskListView,
    TaskCreateView,
    TaskDeleteView,
    TaskUpdateView,
    task_manage,
    TagListView,
    TagCreateView,
    TagUpdateView,
    TagDeleteView
)

urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
    path("task/create/", TaskCreateView.as_view(), name="task-create"),
    path("task/delete/<int:pk>/", TaskDeleteView.as_view(),
         name="task-delete"),
    path("task/update/<int:pk>/", TaskUpdateView.as_view(),
         name="task-update"),
    path("task/manage/<int:pk>/<action>", task_manage, name="task-manage"),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tags/create/", TagCreateView.as_view(), name="tag-create"),
    path("tags/update/<int:pk>", TagUpdateView.as_view(), name="tag-update"),
    path("tags/delete/<int:pk>", TagDeleteView.as_view(), name="tag-delete"),
]

app_name = "todo"
