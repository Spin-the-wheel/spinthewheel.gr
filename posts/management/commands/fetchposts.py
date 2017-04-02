from django.core.management.base import BaseCommand, CommandError
from posts.models import Post
from django.conf import settings

from pytumblr import TumblrRestClient


class Command(BaseCommand):
    help = 'Fetch all posts from tumblr'

    # def add_arguments(self, parser):
    #     parser.add_argument('poll_id', nargs='+', type=int)

    def handle(self, *args, **options):

        client = TumblrRestClient(
        settings.SECRETS.get('tumblr_key'),
        settings.SECRETS.get('tumblr_secret'),
        settings.SECRETS.get('tumblr_oauth_token'),
        settings.SECRETS.get('tumblr_oauth_secret'),
        )

        response = client.posts(settings.BLOG)
        posts = response['posts']

        for post in posts:
            if post['type'] == 'text':
                Post.objects.update_or_create(
                    id=post['id'],
                    defaults={
                        'id':post['id'],
                        'title': post['title'],
                        'url': post['post_url'],
                        'body':post['body'],
                        'date':post['date'][:10],
                        'published':post['state']=='published'
                    },
                )
            elif post['type'] == 'link':
                Post.objects.update_or_create(
                    id=post['id'],
                    defaults={
                        'id':post['id'],
                        'title': post['title'],
                        'url': post['post_url'],
                        'body':post['description'],
                        'date':post['date'][:10],
                        'published':post['state']=='published'
                    },
                )
            elif post['type'] == 'photo':
                Post.objects.update_or_create(
                    id=post['id'],
                    defaults={
                        'id':post['id'],
                        'title': post['summary'],
                        'url': post['post_url'],
                        'body':post['caption'],
                        'date':post['date'][:10],
                        'published':post['state']=='published'
                    },
                )


        self.stdout.write(self.style.SUCCESS('Successfully fetched '))
