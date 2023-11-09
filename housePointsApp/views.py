from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect

from .models import House

def index(request):
    houses = House.objects.order_by('-points')
    context = {
            'houses': houses,
    }
    return render(request, 'housePointsApp/index.html', context)

def addPoints(request):
    houseName = request.POST.get('houseName')
    operation = request.POST.get('operation')
    points = request.POST.get('points')
    students = request.POST.get('students')

    if houseName == '':
        return HttpResponseRedirect('/')

    house = get_object_or_404(House, name=houseName)
    if operation == 'add':
        house.points += int(points)
    elif operation == 'sub':
        house.points -= int(points)
    
    if students != '':
        house.students = students

    house.save()
    return HttpResponseRedirect('/')

def reset(request):
    return render(request, 'housePointsApp/reset.html', {})

def confirmPoints(request):
    houses = House.objects.all()

    for house in houses:
        house.points = 0
        house.save()

    return HttpResponseRedirect('/')

def confirmStudents(request):
    houses = House.objects.all()

    for house in houses:
        house.students = 0
        house.save()

    return HttpResponseRedirect('/')

def confirmAll(request):
    confirmPoints(request)
    confirmStudents(request)

    return HttpResponseRedirect('/')
