from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404, JsonResponse
from django.urls import reverse
from django.shortcuts import render
from .models import Task


def taskList(request):
    tasks = Task.objects.all()
    return render(request, 'index.html', {'tasks': tasks})


def create_task(request):
    a = Task(title=request.POST['title'])
    a.save()
    return HttpResponseRedirect(reverse('ap:tasks'))


def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return HttpResponseRedirect(reverse('ap:tasks'))


def edit_task(request, task_id):
    task = Task.objects.get(id=task_id)


def check_task(request, task_id):
    try:
        task = Task.objects.get(id=task_id)
        task.completed = not task.completed
        task.save()
        response_data = {
            'completed': task.completed
        }
        return JsonResponse(response_data)
    except:
        raise Http404('Task not found')
