from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, 'home.html')

def programmes(request):
    return render(request, 'programmes.html')

def semester(request):
    return render(request, 'semester.html')

def feedback(request):
    return render(request,'feedback.html')

def cs_view(request):
    return render(request, 'cs.html')