from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('index/',diaryindex, name="diaryindex"),
    path('<str:id>',diarydetails, name="diarydetails"),
    path('new/',newdiary,name="newdiary"),
    path('creatediary/',creatediary, name="creatediary"),
    path('diaryupdate/<str:id>',diaryupdate, name="diaryupdate"),
    path('update/<str:id>', update, name="update"),
    path('delete/<str:id>', delete, name="delete"),
]