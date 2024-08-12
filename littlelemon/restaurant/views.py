from django.shortcuts import render
from django.http import HttpRequest
from .models import Booking,Menu
from .serializers import MenuSerializer,BookingSerializer
from rest_framework import generics
from rest_framework import viewsets
# Create your views here.

# def home(request):
#     return HttpRequest("hello guys this is my first try to make a site.")
def index(request):
    return render(request,'index.html')

class MenuView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class=MenuSerializer


class SingleMenuView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
