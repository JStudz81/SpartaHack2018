from django.shortcuts import render


def index(request):
    return render(request, 'index.html', {})

def user_info(request, user_id):
    return