"""sycamore_trees URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from tree_menu.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('page', what_a_view, name='page'),
    path('vitaley', not_a_view, name='vitaley'),
    path('prikol', view_is_gone, name='prikol'),
    path('questionable', policeman_fox, name='questionable'),
    path('mindblow', about_myself, name='mindblow'),
    path('pieleg', one_more_view, name='pieleg'),
    path('whatever', and_another_view, name='whatever'),
    path('unprikol', not_a_view, name='unprikol')

]
