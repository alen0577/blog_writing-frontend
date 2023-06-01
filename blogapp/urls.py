from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('login/',views.login,name='login'),
    path('register/',views.register,name='register'),
    path('blogview/',views.blogview,name='blogview'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('newpost/',views.newpost,name='newpost'),
    path('editpost/',views.editpost,name='editpost'),
]

