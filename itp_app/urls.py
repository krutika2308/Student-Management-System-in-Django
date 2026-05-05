from django.contrib import admin
from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('login/', views.user_login, name='user_login'), 
    path('add/',views.add_student,name='addStudent'),
    path('list/',views.student_list,name='student_list'),
    path('update/<int:id>/',views.update_student,name='update_student'),
    path('delete/<int:id>/',views.delete,name='delete'),
    path('courses/',views.courses, name='courses'),
    path('fees/', views.fees, name='fees'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('blog/',views.blog,name='blog'),
    path('logout/', views.user_logout, name='logout')

]