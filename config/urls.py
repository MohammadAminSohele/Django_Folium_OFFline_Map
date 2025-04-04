"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from maps.views import Show_cordination_Pardis,Show_cordination_Tehran,Show_cordination_Bomehen
from django.conf.urls.static import static

from .import settings

urlpatterns = [
    path('',Show_cordination_Tehran,name='Show_cordination_Tehran'),
    path('Pardis',Show_cordination_Pardis,name='Show_cordination_Pardis'),
    path('Bomehen',Show_cordination_Bomehen,name='Show_cordination_Bomehen'),

    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)