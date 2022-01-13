"""p10 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from p10 import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('func/',views.funcsample,name='func'),
    path('cls/',views.clssample.as_view(),name='cls'),
    path('fselect/',views.funcselect,name='fselect'),
    path('cselect/',views.clsselect.as_view(),name='cselect'),
    path('fupdate/<data>/',views.funcupdate,name='fupdate'),
    path('cupdate/<data>/',views.clsupdate.as_view(),name='cupdate'),
    path('fdelete/<data>/',views.funcdelete,name='fdelete'),
    path('cdelete/<data>/',views.clsdelete.as_view(),name='cdelete'),
    #path('func/<id>/',views.funcsample,name='func'),
    #path('cls/<id>/',views.clssample.as_view(),name='cls'),
]
