from django.shortcuts import render, redirect


# Create your views here.
def index(request):
    return render(request, 'personalsite/index.html')

def resumeView(request):
    return render(request, 'personalsite/resume.html')




