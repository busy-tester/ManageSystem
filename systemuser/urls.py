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
from systemuser.views import LoginView
from systemuser.views import UserinfoView
from systemuser.views import LogoutView
from systemuser.views import RegisterView
from systemuser.views import CheckPwdView
from systemuser.views import UpdatePwdView

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('login', LoginView.as_view()),
    path('info', UserinfoView.as_view()),
    path('logout', LogoutView.as_view()),
    path('register', RegisterView.as_view()),
    path('check/pwd', CheckPwdView.as_view()),
    path('update/pwd', UpdatePwdView.as_view())
]
