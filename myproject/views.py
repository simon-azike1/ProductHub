from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # You can also render a home.html template here if you want
    return render(request, 'home.html')
