from .models import (
    Login,
    Student,
    StudentGroup3,
    StudentGroup4,
    StudentGroup6,
    ReserveStudent,
    Room,
    GroupStudent
)
from django.forms import ModelForm 
from django import forms
class LoginForm(forms.ModelForm):
    class Meta:
        model = Login
        fields = '__all__'

class StudentFullNameForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = '__all__'
class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ["block","room_number"]


class StudentForm(forms.ModelForm):
    class Meta:
        model = GroupStudent
        fields = '__all__'


class StudentGroup3Form(forms.ModelForm):
    class Meta: 
        model = StudentGroup3
        fields =['stu1','stu2','stu3','stu1_tick','stu2_tick','stu3_tick']


class StudentGroup4Form(forms.ModelForm):
    stu1 = StudentForm()
    stu2 = StudentForm()
    stu3 = StudentForm()
    stu4=StudentForm()
    class Meta:
        model = StudentGroup4
        fields = ["stu1", "stu2", "stu3","stu4", "stu1_tick",'stu2_tick','stu3_tick',"stu4_tick"]


class StudentGroup6Form(forms.ModelForm):
    stu1 = StudentForm()
    stu2 = StudentForm()
    stu3 = StudentForm()
    stu4 = StudentForm()
    stu5 = StudentForm()
    stu6 = StudentForm()

    class Meta:
        model = StudentGroup6
        fields = ["stu1", "stu2", "stu3", "stu4","stu5","stu6", "stu1_tick",'stu2_tick','stu3_tick',"stu4_tick","stu5_tick","stu6_tick"]


class ReserveStudentForm(forms.ModelForm):
    class Meta:
        model=ReserveStudent
        fields="__all__"
