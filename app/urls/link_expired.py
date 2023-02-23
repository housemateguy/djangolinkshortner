from django.shortcuts import render

def link_expired(request, token):
    return render(request, 'link_expired.html', {'token': token})