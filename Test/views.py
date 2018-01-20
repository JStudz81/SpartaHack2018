from django.shortcuts import render


def index(request):
    return render(request, 'index.html', {})


def user_info(request):
    # Test.models.objects.get(request)
    print("Found request")
    return