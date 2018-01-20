from django.shortcuts import render
from .models import User


def index(request):
    return render(request, 'index.html', {})


def user_info(request, user_id):
    # Test.models.objects.get(request)
    user = User.objects.get(pk=user_id)
    user.username
    print("Found request")
    return