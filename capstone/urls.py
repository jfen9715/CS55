"""capstone URL Configuration

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
from django.urls import path, re_path
from django.views.generic import TemplateView
from backend.views import Login, Register, Save, GetUserData

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/verify/', Login.as_view(), name='login'),
    path('login/register/', Register.as_view(), name='register'),
    path('login/save/', Save.as_view(), name='save'),
    path('login/data/', GetUserData.as_view(), name='user_data'),
    path('', TemplateView.as_view(template_name='index.html')),
    re_path(r'.*', TemplateView.as_view(template_name='index.html')),
]
