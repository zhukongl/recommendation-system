"""rec_sys_prj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include, re_path
from rec_sys_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('query', views.query),
    path('train', views.train),
    path('login', views.login),
    path('newtransaction', views.newtransaction),

    re_path(r'^rec_sys_app/',include('rec_sys_app.urls')),
    re_path(r'^$', views.index, name="indexx"),
    # re_path(r'help$', include('rec_sys_app.urls'))
]
