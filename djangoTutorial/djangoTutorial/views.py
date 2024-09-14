from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse('Hello, Django!')
    return render(request, 'website/home.html')

def about(request):
    # return HttpResponse('About us')
    return render(request, 'website/about.html')

def contact(request):
    # return HttpResponse('Contact us')
    return render(request, 'website/contact.html')
