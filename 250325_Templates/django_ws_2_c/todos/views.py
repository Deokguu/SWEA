from django.shortcuts import render

# Create your views here.
def index(request):
    print(request)
    work = request.GET.get('work')
    print(work)
    context = {
        'work' : work
    }
    return render(request, 'todos/index.html', context)
    # return render(request, 'todos/index.html')

def create_todo(request):
    return render(request, 'todos/create_todo.html')

def detail(request, work):
    print(work)
    context = {
        'work' : work
    }
    return render(request, 'todos/detail.html', context)
