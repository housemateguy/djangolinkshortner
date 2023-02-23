"""djangolinkshortner URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from app.urls.home import home
from app.urls.link_expired import link_expired
from app.urls.stats import stats
from app.views.redirect import redirect_to_long_url

urlpatterns = [
]
app_name = 'shortener'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('stats/<slug:token>/', stats, name='stats'),
    path('link_expired/<slug:token>/',link_expired , name='link_expired'),
    path('<slug:token>/', redirect_to_long_url, name='redirect_to_long_url'),
]
