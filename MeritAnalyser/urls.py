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
    re_path('ReportCard/',views.ReportCard),

    path('show_report/<str:testid>/',views.show_report),
]