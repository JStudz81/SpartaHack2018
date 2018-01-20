from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Character, CharInst



def index(request):
    user = User.objects.get(pk=2)
    return render(request, 'index.html', {'user': user})



def user_info(request, user_id):
    # Test.models.objects.get(request)
    print("Found request")
