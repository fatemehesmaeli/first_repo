from django.shortcuts import render
from .serializers import (LoginSerializer,
StudentGroup3Serializer,
StudentGroup4Serializer,
StudentGroup6Serializer,
StudentSerializer,
RoomSerializer,
ReserveStudentSerializer)
from .models import (Login,
Student,StudentGroup3,StudentGroup4,StudentGroup6,ReserveStudent,Room)
from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from rest_framework.decorators import permission_classes
# Create your views here.
def index(request):
    return render(request,'index.html')
