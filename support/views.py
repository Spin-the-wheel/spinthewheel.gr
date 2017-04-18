from django.shortcuts import render
from django.http import HttpResponse

from .models import Kind

def index(request):

    kinds = Kind.objects.select_related().order_by('order', 'sponsor__name').all()

    data = {
        'active_tab': 'support',
        'kinds': kinds,
    }

    return render(request, 'support/index.html', data)
