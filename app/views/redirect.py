from django.shortcuts import get_object_or_404, redirect
from app.models.click import Click
from app.models.link import Link

def redirect_to_long_url(request, token):
    link = get_object_or_404(Link, token=token)
    if link.is_expired() is True or link.is_click_limit_reached() is True:
        return redirect('link_expired', token=token)
    link.clicks_count += 1
    click = Click(link=link, ip_address=request.META['REMOTE_ADDR'])
    click.save()
    link.save()
    return redirect(link.original_url)