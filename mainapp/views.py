from django.shortcuts import render
from .models import Issues
import requests


def index(request):
    res = requests.get('https://api.github.com/repos/django/channels/issues').json()
    print(res)

    for item in res:
        i = Issues(
            id_number=int(item['id']),
            url=item['url'],
            title=item['title'],
            comments=int(item['comments']),
        )
        try:
            Issues.objects.all().filter(title=item['title'])[0]
        except IndexError:
            i.save()

    max_comment = Issues.objects.order_by('-comments')[0]
    min_comment = Issues.objects.order_by('comments')[0]
    top_comments = Issues.objects.filter(comments__gte=10)

    return render(request, 'mainapp/index.html',
        {
            'max_comment': max_comment,
            'min_comment': min_comment,
            'top_comments': top_comments,
        }
    )
