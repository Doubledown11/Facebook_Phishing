from django.shortcuts import render

# Create your views here.


def home(request):
    """Sends user to the home page."""
    return render(request, 'login/home.html')