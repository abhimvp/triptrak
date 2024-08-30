"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path,include

from django.conf import settings
from django.conf.urls.static import static #Return a URL pattern for serving files in debug mode.
from .views import SignUpView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('triptrak.urls')),
    path('accounts/',include('django.contrib.auth.urls')), #https://docs.djangoproject.com/en/5.1/topics/auth/
    path('accounts/signup/',SignUpView.as_view(),name='signup'),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
