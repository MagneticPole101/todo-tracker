from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core import serializers
from main.forms import TodoForm
from main.models import Todo

# Create your views here.
def show_main(request):
    todos = Todo.objects.all()

    context = {
        'name': 'Khair J',
        'class': 'PBP A',
        'todos': todos
    }

    return render(request, "main.html", context)

def create_todo(request):
    form = TodoForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_todo.html", context)

def show_xml(request):
    data = Todo.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Todo.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Todo.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Todo.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")