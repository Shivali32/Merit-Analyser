"""AlphaBots URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path,include,re_path
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('MeritAnalyser.urls')),
    re_path('login/',include('MeritAnalyser.urls')),
    re_path('logout/',include('MeritAnalyser.urls')),
    re_path('register/',include('MeritAnalyser.urls')),
    re_path('register_teacher/',include('MeritAnalyser.urls')),
    re_path('register_student/',include('MeritAnalyser.urls')),
    re_path('random/',include('MeritAnalyser.urls')),
    re_path('create_test/',include('MeritAnalyser.urls')),
    re_path('demodashboard/',include('MeritAnalyser.urls')),
    re_path('ReportCard/',include('MeritAnalyser.urls')),

    path('show_report/<str:testid>/',include('MeritAnalyser.urls')),
]
