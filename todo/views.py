
from django.shortcuts import render,HttpResponse
from .import models
from .models import Task
from django.contrib import messages
from django.views.generic import TemplateView,ListView,DetailView


# Create your views here.
def home(request):
    context={
        'success':False,
       
       
    }
    if request.method=="POST":
        t_title=request.POST.get('title')
        d_description=request.POST.get('description')
        i_id=request.POST.get('id')
        print(t_title,d_description)


        ins=Task(title=t_title,description=d_description,id=i_id)
        ins.save()
        context={
            'success':True,
        }
        
    return render(request,'index.html',context)

def about(request):
    allTasks=Task.objects.all() ##fetch all the tasks from modules
    context={
        'tasks':allTasks
    }
    return render(request,'about.html',context)
def delete(request,id):
    obj=Task.objects.get(id=id)
    obj.delete()
    messages.success(request,('item is deleted successfully!!'))
    return render(request,'about.html')

class TaskList(ListView):
    model=models.Task
    context_object_name="task"
    template_name='taskl_list.html'


