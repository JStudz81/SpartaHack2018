from django.shortcuts import render
from .models import User

def index(request):
    return render(request, 'index.html', {})

def user_info(request, user_id):
    user = User.objects.get(pk=1)
    user.username
    print("request received")
    pass