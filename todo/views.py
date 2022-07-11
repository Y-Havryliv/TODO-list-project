from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic

from todo.models import Task, Tag


class TaskListView(generic.ListView):
    model = Task
    ordering = ["done_status", "-created_at"]


class TaskCreateView(generic.CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("todo:task-list")


class TaskDeleteView(generic.DeleteView):
    model = Task
    template_name = "todo/task_confirm_delete.html"
    success_url = reverse_lazy("todo:task-list")


class TaskUpdateView(generic.UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("todo:task-list")


def task_manage(request, pk, action):
    task = Task.objects.get(id=pk)

    if action == "undo":
        task.done_status = False
    if action == "mark_as_done":
        task.done_status = True

    task.save()

    return HttpResponseRedirect(reverse_lazy("todo:task-list"))


class TagListView(generic.ListView):
    model = Tag


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    template_name = "todo/tag_confirm_delete.html"
    success_url = reverse_lazy("todo:tag-list")
