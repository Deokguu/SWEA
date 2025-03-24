from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'todos/index.html')
def creat_todo(request):
    return render(request, 'todos/creat_todo.html')