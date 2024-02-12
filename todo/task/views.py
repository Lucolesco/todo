from django.shortcuts import render
from django.views.generic.base import TemplateView, View
from task.models import Task
# Create your views here.


class MainView(TemplateView):
    template_name = "page/index.html"
    def get(self, request):
        tasks_completed = Task.objects.filter(status=True)
        tasks_in_progress = Task.objects.filter(status=False)
        return render(request, self.template_name, {'tasks_completed': tasks_completed,
                                                    'tasks_in_progress': tasks_in_progress})

