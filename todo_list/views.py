from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import TodoItem

def todo_view(request):
    k=0
    all_todo_items = TodoItem.objects.all()
    return render(request, 'todo.html',
        {'all_todo_items': all_todo_items})

def add_todo(request):
    new_item = TodoItem(content = request.POST['content'])
    all_todo_items = TodoItem.objects.all()
    if TodoItem.objects.filter(content=new_item.content):
        k=1  
        return render(request, 'todo.html',{'k': k,'all_todo_items': all_todo_items})
    else:
        k=0 
        new_item.save()
        return render(request, 'todo.html',{'k': k,'all_todo_items': all_todo_items})
    

def delete_todo(request, todo_id):
    item_to_delete = TodoItem.objects.get(id=todo_id)
    item_to_delete.delete()
    return HttpResponseRedirect('/todo/')
