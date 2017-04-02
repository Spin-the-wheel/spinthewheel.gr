from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import GalleryImage, Gallery

def index(request):

    galleries = Gallery.objects.all()

    data = {
        'galleries': galleries
    }

    return render(request, 'gallery/index.html', data)

def folder(request, slug):

    gallery = get_object_or_404(Gallery, slug=slug)

    images = gallery.images.all()

    data={
        'gallery': gallery,
        'images': images
    }

    return render(request, 'gallery/folder.html', data)