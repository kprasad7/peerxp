from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Indexpage),
    path('signup/', views.Post , name="Post"),
    path('signin/' , views.loginuser , name="loginuser")
]
