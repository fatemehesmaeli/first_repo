from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
from .models import Booking,Menu
from .serializers import MenuSerializer,BookingSerializer
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser,IsAuthenticated
from rest_framework.decorators import parser_classes

# Create your views here.

# def home(request):
#     return HttpRequest("hello guys this is my first try to make a site.")
def index(request):
    return render(request,'index.html')

class MenuView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class=MenuSerializer
    def get_permissions(self):
        permission_classes=[]
        if self.request.method != 'GET':

            permission_classes=[IsAdminUser]
        return [permission() for permission in permission_classes]
    
        


class SingleMenuView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    def get_permissions(self):
        permission_classes=[]
        if self.request.method != 'GET':

            permission_classes=[IsAdminUser]
        return [permission() for permission in permission_classes]


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

