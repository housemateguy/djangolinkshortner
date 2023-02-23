from django.shortcuts import render, get_object_or_404
from app.models.click import Click
from app.models.link import Link

def stats(request, token):
    link = get_object_or_404(Link, token=token)
    clicks = Click.objects.filter(link=link).order_by('-timestamp')
    context = {
        'link': link,
        'clicks': clicks,
    }
    return render(request, 'stats.html', context)