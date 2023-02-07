from django.shortcuts import render,redirect
from .models import List,Task,Profile
from .forms import ListForm,ShareForm,TaskFormSet
from django.contrib.auth.decorators import login_required
from django import forms
from django.contrib import messages

@login_required(login_url='login')
def dashboard(request):
    profile = request.user.profile
    lists = profile.list_set.all()
    shared_lists = profile.sharing.all()
    result_list = lists|shared_lists

    if request.GET:
        print(request.GET)
        task_id = request.GET['task']
        task = Task.objects.get(id=task_id)
        if task.completed:
            task.completed = False
            task.save()
        else:
            task.completed = True
            task.save()
    
    context  ={'lists':result_list }
    return render(request,'lists/dashboard.html',context)


@login_required(login_url='login')
def list(request,pk):
    list = List.objects.get(id=pk)
    queryset = Task.objects.filter(owner_list=list)


    if request.method == 'POST':
        if 'taskform-0-name' in request.POST:
            formset = TaskFormSet(request.POST,queryset=queryset,prefix='taskform')
            if formset.is_valid():
                instances = formset.save(commit=False)

                for instance in instances:
                    instance.owner_list =list
                    instance.save()
                return redirect('list',pk=list.id)

        elif 'title' in request.POST:

            form = ListForm(request.POST,instance=list)
            if form.is_valid():
                form.save()   
                return redirect('list',pk=list.id)
    else:
        formset = TaskFormSet(prefix='taskform',queryset=queryset)
        form = ListForm(instance=list)

    context = {'pk':pk, 'list':list,'formset':formset,'queryset':queryset,'form':form}
    return render(request,'lists/list.html',context)


@login_required(login_url='login')
def createList(request):
    profile = request.user.profile
    form = ListForm()

    if request.method == "POST":
        form = ListForm(request.POST)
        if form.is_valid():
            list = form.save(commit=False)
            list.owner = profile
            list.save()       
        return redirect('list',pk=list.id)

    context={'form':form}
    return render(request,'lists/list_form.html',context)

@login_required(login_url='login')
def deleteList(request,pk):
    list = List.objects.get(id=pk)

    if request.method == 'POST':
        list.delete()
        return redirect('dashboard')
        
    context = {'object':list}
    return render(request,'delete-template.html',context)

def shareList(request,pk):
    list = List.objects.get(id=pk)
    form = ShareForm()

    if request.method =='POST':
        form=ShareForm(request.POST)
        print(form)
        if form.is_valid():
            try:
                invited_user = Profile.objects.get(username=request.POST['coowner'])
                list.coowner= invited_user
                list.save()
                messages.success(request,'List successfully shared with: '+ invited_user.name)
            except:
                try:
                    invited_user = Profile.objects.get(email=request.POST['coowner'])
                    list.coowner= invited_user
                    list.save()
                    messages.success(request,'List successfully shared with: '+ invited_user.name)
                except:                    
                    messages.warning(request,'User was not found!')       
                return redirect('dashboard') 

        return redirect('dashboard')
    if request.GET:
        list.coowner = None
        list.save()
        messages.info(request,'You are not sharing List: '+ list.title + ' anymore.') 
        return redirect('dashboard')


    context={'list':list,'form':form}
    return render(request,'lists/share_form.html',context)

@login_required(login_url='login')
def deleteTask(request,pk):
    task = Task.objects.get(id=pk)

    if request.method =='POST':
        task.delete()
        return redirect('list',pk = task.owner_list.id)

    context ={'object':task}
    return render(request,'delete-template.html',context)

