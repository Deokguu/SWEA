from django.shortcuts import render, redirect
from .models import Garage

# Create your views here.
def index(request):
    garages = Garage.objects.all()
    context = {
        'garages': garages
    }
    return render(request, 'garages/index.html', context)

def new(request):
    return render(request, 'garages/new.html')

def create(request):
    location = request.POST.get('location')
    capacity = request.POST.get('capacity')
    is_parking_avaliable = request.POST.get('is_parking_avaliable')
    opening_time = request.POST.get('opening_time')
    closing_time = request.POST.get('closing_time')

    garage = Garage(location=location,capacity=capacity,is_parking_avaliable=is_parking_avaliable,opening_time=opening_time,closing_time=closing_time)
    garage.save()
    return redirect('garages:index')

def edit(request, garage_pk):
    garage = Garage.objects.get(pk=garage_pk)

    return render(request, 'garages/edit.html', {'garage':garage})

def update(request, garage_pk):
    garage = Garage.objects.get(pk=garage_pk)
    print(request)
    print(request.POST)
    garage.location = request.POST.get('location')
    garage.capacity = request.POST.get('capacity')
    garage.is_parking_avaliable = request.POST.get('is_parking_avaliable')
    garage.opening_time = request.POST.get('opening_time')
    garage.closing_time = request.POST.get('closing_time')

    garage.save()
    return
    # return redirect('garages:index')

def delete(request, garage_pk):
    #DB로부터 읽어오기(조회)
    garage = Garage.objects.get(pk=garage_pk)
    garage.delete()

    return redirect('garages:index')