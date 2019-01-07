"""monitor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url, include
from django.urls import path
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token, refresh_jwt_token
from . import views

router = routers.DefaultRouter()

urlpatterns = [
    # url(r'^', include(router.urls)),
    path('api/admin/auth/', obtain_jwt_token),
    path('api/admin/verify/', verify_jwt_token),
    path('api/admin/refresh/', refresh_jwt_token),
    path('api/cpu/info/', views.cpu_info),
    path('api/memory/info/', views.memory_info),
    path('api/cpumemory/info/', views.cpu_memory_info),
    path('api/netdisk/io/', views.net_disk_io),
    path('api/net/analyze/', views.net_analyze),
    path('api/battery/info/', views.battery_percent),
    path('api/log/analyze/', views.log_analyze),

]
