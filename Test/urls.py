"""Test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('login/', views.showLogin, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('game/<int:game_id>', views.game_view, name='game'),
    path('character/<int:character_id>', views.character_view, name='character'),
    path('user/<int:user_id>/', views.user_info, name='User stats'),
    path('character_info/<int:character_id>', views.character_info, name='Character Stats'),
    path('addGame/', views.addGame, name='addGame'),
    path('addStat/<int:character_id>', views.addStat, name='addStat'),
    path('addCharacter/<int:game_id>', views.addCharacter, name='addCharacter'),
    path('search/', views.search, name='search'),
    path('battles/', views.battles, name='battles'),
    path('allGames/', views.allGames, name='allGames'),
    #path('<int:char_id>/', views.char)
]

#testing gitignore