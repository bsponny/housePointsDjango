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
    points = request.POST.get('points')
    students = request.POST.get('students')

    if houseName == '' or points == '':
        return HttpResponseRedirect('/')

    house = get_object_or_404(House, name=houseName)
    if points == 'add5':
        house.points += 5
    elif points == 'sub5':
        house.points -= 5
    elif points == 'add10':
        house.points += 10
    elif points == 'sub10':
        house.points -= 10
    
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

