from django.shortcuts import render
from django.http import HttpRequest
# Create your views here.

# def home(request):
#     return HttpRequest("hello guys this is my first try to make a site.")
def index(request):
    return render(request,'index.html')