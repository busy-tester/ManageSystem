"""ManageSystem URL Configuration

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
from django.contrib import admin
from django.urls import path, include
from systemapp.views.member import MemberView, SearchMemberView
from systemapp.views.supplier import SupplierView, SearchSupplierView
from systemapp.views.staff import StaffView, SearchStaffView

urlpatterns = [
    path('member', MemberView.as_view()),
    path('supplier', SupplierView.as_view()),
    path('staff', StaffView.as_view()),
    path('search/member', SearchMemberView.as_view()),
    path('search/supplier', SearchSupplierView.as_view()),
    path('search/staff', SearchStaffView.as_view()),
]