from django.shortcuts import render,redirect
from Todolist.models import Task
from Todolist.forms import TaskForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

def homepage(request):
    return render(request,"main.html",{})


@login_required
def todolist(request):
    if request.method == "POST":
        form_data=TaskForm(request.POST or None )
        if form_data.is_valid():
            instance = form_data.save(commit=False)
            instance.owner = request.user
            instance.save()
            messages.success(request,"Task Added Successfully.")
            return redirect("todolist")
        
        messages.success(request,"Something went Wrong !")
    
    tasks = Task.objects.filter(owner = request.user)
    paginator = Paginator(tasks , 8)
    page = request.GET.get("page")
    tasks = paginator.get_page(page)
    
    return render(request, 'todolist.html', {'tasks': tasks})

@login_required
def delete_task(request, task_id):
    task_obj = Task.objects.get(id = task_id)
    if task_obj.owner == request.user: 
        task_obj.delete()
        messages.success(request , f"Task - {task_obj.task} deleted.")
    else:
        messages.error(request,"ACCESS DENIED !")
    return redirect("todolist")


@login_required
def edit_task(request, task_id):
    task_obj = Task.objects.get(id = task_id)
    
    if request.method == "POST":
        form_data = TaskForm(request.POST or None , instance=task_obj)
        if form_data.is_valid():
            form_data.save()
            messages.success(request,"Task Updated.")
            return redirect("todolist")
        messages.success(request,"Error Encounter in Task Updation !")
    else:
      context = {
        'task_obj' : task_obj
       }
    return render(request,"edit.html",context)


@login_required
def complete_task(request , task_id):
    task_obj = Task.objects.get(id = task_id)
    if task_obj.owner == request.user: 
        task_obj.is_completed=True
        task_obj.save()
        messages.success(request,"Task is completed Successfully.")
    else:
        messages.error(request,"You're not allowed to change status.")
    return redirect("todolist")


@login_required
def pending_task(request , task_id):
    task_obj = Task.objects.get(id = task_id)
    if task_obj.owner == request.user: 
        task_obj.is_completed=False
        task_obj.save()
        messages.success(request,"Task is not completed.")
    else:
        messages.error(request,"You're not allowed to change status.")    
    return redirect("todolist")
    

def contact(request):
    return render(request,"contact.html",{})


def about(request):
    return render(request,"about.html",{})