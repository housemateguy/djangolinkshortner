from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils import timezone
from app.models.link import Link

def home(request):
    if request.method == 'POST':
        original_url = request.POST.get('url')
        max_clicks = int(request.POST.get('max_clicks', 0))
        expiration_days = int(request.POST.get('expiration_days', 0))
        link = Link(original_url=original_url, max_clicks=max_clicks)
        if expiration_days > 0:
            link.expiration_date = timezone.now() + timezone.timedelta(days=expiration_days)
        link.save()
        link.generate_token()
        link.generate_short_url()
        link.save()
        # once the link is created, redirect to the stats page
        return redirect(reverse('stats', args=[link.token]))
    return render(request, 'home.html')
