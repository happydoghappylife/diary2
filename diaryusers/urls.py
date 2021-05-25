from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('userlogin/',userlogin,name="userlogin"),
    path('userlogout/',userlogout,name="userlogout"),
    path('userregister/',userregister,name="userregister"),
]