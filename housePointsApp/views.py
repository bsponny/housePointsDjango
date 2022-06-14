from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect

from .models import House

def index(request):
    houses = House.objects.all()
    context = {
            'houses': houses,
    }
    return render(request, 'housePointsApp/index.html', context)

def addPoints(request):
    houseName = request.POST.get('houseName')
    points = request.POST.get('points')

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

    house.save()
    return HttpResponseRedirect('/')

def reset(request):
    houses = House.objects.all()

    for house in houses:
        house.points = 0
        house.save()

    return HttpResponseRedirect('/')

