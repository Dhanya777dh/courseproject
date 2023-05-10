from django.urls import path,include
from . import views
from unicodedata import name

urlpatterns = [
   path('',views.demofun,name='demofun'),
   path('loginpage',views.loginpage,name='loginpage'),
   path('signup',views.signup,name='signup'),
   path('add_course',views.add_course,name='add_course'),
   path('add_student',views.add_student,name='add_student'),
   path('logoutpage',views.logoutpage,name='logoutpage'),

   path('login1',views.login1,name='login1'),
   path('usercreate',views.usercreate,name='usercreate'),
   path('logout',views.logout,name='logout'),
   path('add_course_details',views.add_course_details,name='add_course_details'),
   path('add_student_details',views.add_student_details,name='add_student_details'),
   path('showstudentdetails',views.showstudentdetails,name='showstudentdetails')
]