from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from main.forms import TodoForm
from main.models import Todo

# Create your views here.
@login_required(login_url='/login')
def show_main(request):
    todos = Todo.objects.filter(user=request.user)

    context = {
        'name': request.user.username,
        'class': 'PBP A',
        'todos': todos,
        'last_login': request.COOKIES['last_login'],
    }

    return render(request, "main.html", context)

def create_todo(request):
    form = TodoForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        todo = form.save(commit=False)
        todo.user = request.user
        todo.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_todo.html", context)

def edit_todo(request, id):
    # Get todo berdasarkan ID
    todo = Todo.objects.get(pk = id)

    # Set todo sebagai instance dari form
    form = TodoForm(request.POST or None, instance=todo)

    if form.is_valid() and request.method == "POST":
        # Simpan form dan kembali ke halaman awal
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_todo.html", context)

def delete_todo(request, id):
    # Get data berdasarkan ID
    todo = Todo.objects.get(pk = id)
    # Hapus data
    todo.delete()
    # Kembali ke halaman awal
    return HttpResponseRedirect(reverse('main:show_main'))

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

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

