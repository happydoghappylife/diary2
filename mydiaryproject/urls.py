"""mydiaryproject URL Configuration

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
#from mydiaryproject.mydiaryapp.views import diarycover, diaryindex
#from mydiaryproject.mydiaryapp.views import newdiary
#from mydiaryproject.mydiaryapp.views import creatediary
#from mydiaryproject.mydiaryapp.views import diaryupdate
#from mydiaryproject.mydiaryapp.views import update
#from mydiaryproject.mydiaryapp.views import delete
from django.contrib import admin
from django.urls import path, include
from django.urls.conf import include
from mydiaryapp.views import diarycover, diaryindex
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', diarycover, name="diarycover"),
    path('index/',diaryindex, name="diaryindex"),
    path('mydiaryapp/',include('mydiaryapp.urls')),
    path('diaryusers/',include('diaryusers.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
