from django.shortcuts import get_object_or_404, redirect, render
from .models import Todo
from .forms import TodoAddForm
# Create your views here.
def home(request):
    return render(request, "todo/home.html")

def list_todo(request):
        todos = Todo.objects.all()
        context = {
            "todos" : todos
        }

        return render(request, "todo/todo_list.html", context)

def create_todo(request):
    form = TodoAddForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("list-todo")

    context = {
        "form": form
    }
    return render(request, 'todo/todo_create.html', context)

def update_todo(request, id):
    # todo = Todo.objects.get(id=id)
    todo = get_object_or_404(Todo, id=id)
    form = TodoAddForm(instance=todo)
    if request.method == "POST":
        form = TodoAddForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect("list-todo")
    context = {
        "form":form
    }

    return render (request, "todo/todo_update.html", context)


def detail_todo(request, id):
    todo = get_object_or_404(Todo, id=id)
    context = {
        "todo" : todo
    }

    return render(request, "todo/todo_detail.html", context)

def delete_todo(request, id):
    todo = get_object_or_404(Todo, id=id)

    if request.method == "POST":
        todo.delete()
        return redirect("list-todo")

    context={
        "todo":todo
        }

    return render(request, "todo/todo_delete.html", context)
