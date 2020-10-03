from django.urls import path,include,re_path
from . import views

urlpatterns = [
    path('',views.index),
    re_path('login/',views.login),
    re_path('register/',views.register),
    re_path('register_teacher/',views.register_teacher),
    re_path('register_student/',views.register_student),
    re_path('random/',views.random_func),
    re_path('create_test/',views.create_test),
    re_path('demodashboard/',views.demodashboard),
    re_path('ReportCard/',views.show_report),
    re_path('logout_request',views.logout_request),
    path('show_report/<str:testid>/',views.show_report),
    path('showstudentreport/<str:studentid>/',views.show_student_report),
    path('dashboard_student/',views.dashboard_student),
    
]