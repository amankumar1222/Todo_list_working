from django.shortcuts import render , redirect ,get_object_or_404
from home.models import Task 

# Create your views here.


def index(request):
    context = {"sucess":False}
    if request.method== 'POST':
        # Handle the form
        title = request.POST['title']
        desc = request.POST['desc']
        print(title, desc)
        ins = Task(taskTitle=title, taskDesc = desc)
        ins.save()
        context = {"success":True}
    return render(request, 'index.html', context)
    
def task(request):
    allTask = Task.objects.all()
    context = {'tasks':allTask}
    return render(request, 'task.html', context)

def deleteTask(request,id):
    task = Task.objects.all().filter(id=id)
    task.delete()
    return redirect('/task')

# def update_data(request, id):
#     if request.method == "POST":
#         pi = User.objects.get(pk=id)
#         fm = StudentRegistration(request.POST, instance=pi)
#         if fm.is_valid():
#             fm.save()
#     else:
#         pi = User.objects.get(pk=id)
#         fm = StudentRegistration(instance=pi)
#     return render(request, 'enroll/updatestudent.html', {'form':fm})

def edit(request,id):

    task = get_object_or_404(Task, id=id)

    if request.method == 'POST':
        # Handle the form
        title = request.POST.get('title', '')
        desc = request.POST.get('desc', '')

        # Update the existing task with the new data
        task.taskTitle = title
        task.taskDesc = desc
        task.save()

        return redirect('/task/')

    else:
        pi = Task.objects.get(pk=id)
        fm = {'form':pi}
        


    return render(request, 'edit.html'  , fm )



