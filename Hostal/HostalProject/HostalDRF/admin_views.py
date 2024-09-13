from django.shortcuts import render
from .serializers import (
    LoginSerializer,
    StudentGroup3Serializer,
    StudentGroup4Serializer,
    StudentGroup6Serializer,
    StudentSerializer,
    RoomSerializer,
    ReserveStudentSerializer,
)
from .models import (
    Login,
    Student,
    StudentGroup3,
    StudentGroup4,
    StudentGroup6,
    ReserveStudent,
    Room,
)
from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from rest_framework.decorators import permission_classes


# Create your views here.

class StudentView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAdminUser]


class SingleStudentView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAdminUser]


class StudentGroup3View(generics.ListCreateAPIView):
    queryset = StudentGroup3.objects.all()
    serializer_class = StudentGroup3Serializer
    permission_classes = [IsAdminUser]


class SingleStudentGroup3View(generics.RetrieveUpdateDestroyAPIView):
    queryset = StudentGroup3.objects.all()
    serializer_class = StudentGroup3Serializer
    permission_classes = [IsAdminUser]


class StudentGroup4View(generics.ListCreateAPIView):
    queryset = StudentGroup4.objects.all()
    serializer_class = StudentGroup4Serializer
    permission_classes = [IsAdminUser]


class SingleStudentGroup4View(generics.RetrieveUpdateDestroyAPIView):
    queryset = StudentGroup4.objects.all()
    serializer_class = StudentGroup6Serializer
    permission_classes = [IsAdminUser]


class StudentGroup6View(generics.ListCreateAPIView):
    queryset = StudentGroup6.objects.all()
    serializer_class = StudentGroup6Serializer
    permission_classes = [IsAdminUser]


class SingleStudentGroup6View(generics.RetrieveUpdateDestroyAPIView):
    queryset = StudentGroup6.objects.all()
    serializer_class = StudentGroup6Serializer
    permission_classes = [IsAdminUser]


class RoomView(generics.ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [IsAdminUser]


class SingleRoomView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [IsAdminUser]


class ReserveStudentView(generics.ListCreateAPIView):
    queryset = ReserveStudent.objects.all()
    serializer_class = ReserveStudentSerializer
    permission_classes = [IsAdminUser]


class SingleReserveStudentView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ReserveStudent.objects.all()
    serializer_class = ReserveStudentSerializer
    permission_classes = [IsAdminUser]


class LoginView(generics.CreateAPIView):
    queryset = Login.objects.all()
    serializer_class = LoginSerializer
    permission_classes = [IsAdminUser]


class SingleLoginView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Login.objects.all()
    serializer_class = LoginSerializer
    permission_classes = [IsAdminUser]
