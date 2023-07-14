from django.shortcuts import render

from django.core.paginator import Paginator

from .models import Menu, Event



def index(request):

    dishes = Menu.objects.all()
    mainDishes = Menu.objects.filter(category__name='Full').order_by('?')
    mainEvent = Event.objects.all().order_by('-date_time')

    paginator = Paginator(mainDishes, 6)
    Event_paginator = Paginator(mainEvent, 3)
    
    page = request.GET.get('page', 1)
    eventPage = request.GET.get('eventPage', 1)

    query = paginator.page(page)
    Event_query = Event_paginator.page(eventPage)


    context = {
        'dishes': dishes,
        'paginator': query,
        'eventPaginator': Event_query,
    }
    return render(request, 'templates/index.html', context)