from django.shortcuts import render
from django.http import HttpResponse

from posts.models import Post, Video

def index(request):

    post = Post.objects.order_by('-date').filter(published=True)[0]

    videos = Video.objects.all()[0]

    data= {
        'active_tab': 'home',
        'post': post,
        'videos': videos,
    }

    return render(request, 'home.html', data)

def get_involved(request):

    data = {
        'active_tab': 'involved'
    }

    return render(request, 'involved.html', data)