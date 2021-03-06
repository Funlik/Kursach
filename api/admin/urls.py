"""admin URL Configuration

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
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.api_index, name='api_index'),
    path('createChat/', views.api_createChat, name='api_createChat'),
    path('users/', views.api_users, name='api_users'),
    path('createMessage/', views.api_createMessage, name='api_createMessage'),
    path('signin/', views.api_signin, name='api_signin'),
    path('registration/', views.api_registration, name='api_registration'),
    path('getMessagesByChatId/', views.api_getMessagesByChatId, name='api_getMessagesByChatId'),
    path('getAllChatByUser/', views.api_getAllChatByUser,name='api_getAllChatByUser'),
    path('changeUsername/', views.api_changeUsername, name='api_changeUsername'),
    path('addUserToChatByUsername/', views.api_addUserToChatByUsername, name='api_addUserToChatByUsername'),



]