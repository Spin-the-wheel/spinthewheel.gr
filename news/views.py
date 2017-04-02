from django.shortcuts import render
from django.http import HttpResponse
from django.utils.dateparse import parse_date
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from posts.models import Post

def index(request):

    posts = Post.objects.order_by('-date').filter(published=True).all()

    paginator = Paginator(posts, 6) # Show 6 posts per page

    page = request.GET.get('page')
    try:
        paginated_posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        paginated_posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        paginated_posts = paginator.page(paginator.num_pages)

    data = {
        'active_tab': 'news',
        'posts': posts,
        'paginated_posts': paginated_posts
    }

    return render(request, 'news/index.html', data)