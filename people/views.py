from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Person, Role

def index(request):

    persons = Person.objects.order_by('role__order', 'name').all()
    paginator = Paginator(persons, 6) # Show 6 persons per page

    page = request.GET.get('page')
    try:
        people = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        people = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        people = paginator.page(paginator.num_pages)

    data = {
        'active_tab': 'people',
        'persons': persons,
        'people' : people
    }

    return render(request, 'people/index.html', data)
