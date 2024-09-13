from .forms import (
    LoginForm,
    StudentForm,
    StudentGroup3Form,
    StudentGroup4Form,
    StudentGroup6Form,
    ReserveStudentForm,StudentFullNameForm,RoomForm
)
from django.shortcuts import render
from django.core import serializers
from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from django.http  import HttpResponse,JsonResponse
from rest_framework.decorators import permission_classes, api_view
from .models import (
    Login,
    Student,
    StudentGroup3,
    StudentGroup4,
    StudentGroup6,
    ReserveStudent,
    Room,GroupStudent
)
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.forms import inlineformset_factory
from django.shortcuts import redirect
from functools import wraps
from django.forms.models import model_to_dict
from decimal import Decimal
from django.db.models import F

def student_login_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if "student_id" in request.session:
            return view_func(request, *args, **kwargs)
        else:
            return redirect("log_in")

    return _wrapped_view

def log_in(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            student = Student.objects.filter(
                student_user=cd["username"], student_password=cd["password"]
            ).first()
            if student:
                request.session["student_id"] = student.id
                return redirect("get_querysets")
            else:
                return JsonResponse({"a": "This account doesn't exist."})
    return render(request, "login.html", {"form": form})

@student_login_required
def get_querysets(request):
    student_id = request.session.get("student_id")
    student_is = Student.objects.get(id=student_id)
    if request.method == "GET":
        form = StudentFullNameForm(instance=student_is)
        return render(request, "account.html", {"form": form, "student": student_is})

    if request.method == "POST":
        form = StudentFullNameForm(request.POST, instance=student_is)
        if form.is_valid():
            cd=form.cleaned_data
            if (cd["end_day"]!=student_is.end_day or 
            cd["start_day"]!=student_is.start_day or 
            cd["room_is"]!=student_is.room_is or 
            cd["admin_tick"]!=student_is.admin_tick or
            cd["billing"]!=student_is.billing):
                return JsonResponse({"error":"You cant Change this item"})
            else:
                student_is.student_password=cd["student_password"]
                student_is.student_user=cd["student_user"]
                student_is.in_group=cd["in_group"]
                student_is.stu_tick=cd["stu_tick"]
                form.save()
                if StudentGroup3.objects.filter(stu1=student_is):
                    stug3=StudentGroup3.objects.get(stu1=student_is)
                    stug3.stu1_tick=student_is.stu_tick
                    stug3.save()
                elif StudentGroup3.objects.filter(stu2=student_is):
                    stug3=StudentGroup3.objects.get(stu2=student_is)
                    stug3.stu2_tick=student_is.stu_tick
                    stug3.save()
                elif StudentGroup3.objects.filter(stu3=student_is):
                    stug3=StudentGroup3.objects.get(stu3=student_is)
                    stug3.stu3_tick=student_is.stu_tick
                    stug3.save()


                elif StudentGroup4.objects.filter(stu1=student_is):
                    stug4=StudentGroup4.objects.get(stu1=student_is)
                    stug4.stu1_tick=student_is.stu_tick
                    stug4.save()
                elif StudentGroup4.objects.filter(stu2=student_is):
                    stug4=StudentGroup4.objects.get(stu2=student_is)
                    stug4.stu2_tick=student_is.stu_tick
                    stug4.save()
                elif StudentGroup4.objects.filter(stu3=student_is):
                    stug4=StudentGroup4.objects.get(stu3=student_is)
                    stug4.stu3_tick=student_is.stu_tick
                    stug4.save()
                elif StudentGroup4.objects.filter(stu4=student_is):
                    stug4=StudentGroup4.objects.get(stu4=student_is)
                    stug4.stu4_tick=student_is.stu_tick
                    stug4.save()

                elif StudentGroup6.objects.filter(stu1=student_is):
                    stug6=StudentGroup6.objects.get(stu1=student_is)
                    stug6.stu1_tick=student_is.stu_tick
                    stug6.save()
                elif StudentGroup6.objects.filter(stu2=student_is):
                    stug6=StudentGroup6.objects.get(stu2=student_is)
                    stug6.stu2_tick=student_is.stu_tick
                    stug6.save()
                elif StudentGroup6.objects.filter(stu3=student_is):
                    stug6=StudentGroup6.objects.get(stu3=student_is)
                    stug6.stu3_tick=student_is.stu_tick
                    stug6.save()
                elif StudentGroup6.objects.filter(stu4=student_is):
                    stug6=StudentGroup6.objects.get(stu4=student_is)
                    stug6.stu4_tick=student_is.stu_tick
                    stug6.save()
                elif StudentGroup6.objects.filter(stu5=student_is):
                    stug6=StudentGroup6.objects.get(stu5=student_is)
                    stug6.stu5_tick=student_is.stu_tick
                    stug6.save()
                elif StudentGroup6.objects.filter(stu6=student_is):
                    stug6=StudentGroup6.objects.get(stu6=student_is)
                    stug6.stu6_tick=student_is.stu_tick
                    stug6.save()

                return JsonResponse({"success": "Information updated successfully."})
        else:
            return JsonResponse({"error": "Invalid data."})
    return render(request, "account.html", {"form": form})

def group3(request):
    student_id = request.session.get("student_id")
    student_is = Student.objects.get(id=student_id)
    stu1 = StudentForm(prefix="stu1")
    stu2 = StudentForm(prefix="stu2")
    stu3 = StudentForm(prefix="stu3")

    if request.method == "POST":
        stu1 = StudentForm(request.POST, prefix="stu1")
        stu2 = StudentForm(request.POST, prefix="stu2")
        stu3 = StudentForm(request.POST, prefix="stu3")

        if stu1.is_valid() and stu2.is_valid() and stu3.is_valid():
            if(student_is.student_user==stu1.cleaned_data["student_user"]):
                if (Student.objects.filter(student_user=stu1.cleaned_data["student_user"]).exists() and
            Student.objects.filter(student_user=stu2.cleaned_data["student_user"]).exists()
            and Student.objects.filter(student_user=stu3.cleaned_data["student_user"]).exists()):
                    student1=Student.objects.get(student_user=stu1.cleaned_data["student_user"])
                    student2=Student.objects.get(student_user=stu2.cleaned_data["student_user"])
                    student3=Student.objects.get(student_user=stu3.cleaned_data["student_user"])
                    if (student1.admin_tick==True and student2.admin_tick==True and student3.admin_tick==True):
                        if(student1.in_group==False and student2.in_group==False and student3.in_group==False):

                            student1.end_day=stu1.cleaned_data["end_day"]
                            student2.end_day=stu2.cleaned_data["end_day"]
                            student3.end_day=stu3.cleaned_data["end_day"]

                            student1.start_day=stu1.cleaned_data["start_day"]
                            student2.start_day=stu2.cleaned_data["start_day"]
                            student3.start_day=stu3.cleaned_data["start_day"]

                            student1.in_group=True
                            student2.in_group=True
                            student3.in_group=True

                            student1.save()
                            student2.save()
                            student3.save()

                            stu1.save()
                            stu2.save()
                            stu3.save()
                            StudentGroup3.objects.create(group_name=student1.student_user,stu1=student1,stu2=student2,stu3=student3
                            ,stu1_tick=True,stu2_tick=False,stu3_tick=False)
                            return JsonResponse({"success":"update informations."})
                        else:
                            return JsonResponse({"error":"the student already in Group"})

                    else:
                        return JsonResponse({"error":"admin_tick is False."})
            else:
                return JsonResponse({"error":"This user dont Login"})
        else:
            return JsonResponse({"error":"Invalid Data"})


    dicti={"stu1":stu1,"stu2":stu2,"stu3":stu3}
    return render(request,'group3.html',dicti)

def group4(request):
    student_id = request.session.get("student_id")
    student_is = Student.objects.get(id=student_id)
    stu1 = StudentForm(prefix="stu1")
    stu2 = StudentForm(prefix="stu2")
    stu3 = StudentForm(prefix="stu3")
    stu4 = StudentForm(prefix="stu4")
    if request.method == "POST":
        stu1 = StudentForm(request.POST, prefix="stu1")
        stu2 = StudentForm(request.POST, prefix="stu2")
        stu3 = StudentForm(request.POST, prefix="stu3")
        stu4 = StudentForm(request.POST, prefix="stu4")
        if stu1.is_valid() and stu2.is_valid() and stu3.is_valid() and stu4.is_valid():
            if(student_is.student_user==stu1.cleaned_data["student_user"]):
                if (Student.objects.filter(student_user=stu1.cleaned_data["student_user"]).exists() and
            Student.objects.filter(student_user=stu2.cleaned_data["student_user"]).exists()
            and Student.objects.filter(student_user=stu3.cleaned_data["student_user"]).exists()
            and Student.objects.filter(student_user=stu4.cleaned_data["student_user"]).exists()):
            
                    student1=Student.objects.get(student_user=stu1.cleaned_data["student_user"])
                    student2=Student.objects.get(student_user=stu2.cleaned_data["student_user"])
                    student3=Student.objects.get(student_user=stu3.cleaned_data["student_user"])
                    student4=Student.objects.get(student_user=stu4.cleaned_data["student_user"])

                    if (student1.admin_tick==True and student2.admin_tick==True and student3.admin_tick==True and student4.admin_tick==True):
                        if(student1.in_group==False and student2.in_group==False and student3.in_group==False and student4.in_group==False):

                            student1.end_day=stu1.cleaned_data["end_day"]
                            student2.end_day=stu2.cleaned_data["end_day"]
                            student3.end_day=stu3.cleaned_data["end_day"]
                            student4.end_day=stu4.cleaned_data["end_day"]

                            student1.start_day=stu1.cleaned_data["start_day"]
                            student2.start_day=stu2.cleaned_data["start_day"]
                            student3.start_day=stu3.cleaned_data["start_day"]
                            student4.start_day=stu4.cleaned_data["start_day"]

                            student1.in_group=True
                            student2.in_group=True
                            student3.in_group=True
                            student4.in_group=True

                            student1.save()
                            student2.save()
                            student3.save()
                            student4.save()

                            stu1.save()
                            stu2.save()
                            stu3.save()
                            stu4.save()

                        
                            StudentGroup4.objects.create(group_name=student1.student_user,stu1=student1,stu2=student2,stu3=student3,stu4=student4
                            ,stu1_tick=True,stu2_tick=False,stu3_tick=False,stu4_tick=False)
                            return JsonResponse({"success":"update informations."})
                        else:
                            return JsonResponse({"error":"the student already in Group"})

                    else:
                        return JsonResponse({"error":"admin_tick is False."})
            else:
                return JsonResponse({"error":"This user dont Login"})
        else:
            return JsonResponse({"error":"Invalid Data"})


    dicti={"stu1":stu1,"stu2":stu2,"stu3":stu3,"stu4":stu4}
    return render(request,'group4.html',dicti)

def group6(request):
    student_id = request.session.get("student_id")
    student_is = Student.objects.get(id=student_id)
    stu1 = StudentForm(prefix="stu1")
    stu2 = StudentForm(prefix="stu2")
    stu3 = StudentForm(prefix="stu3")
    stu4 = StudentForm(prefix="stu4")
    stu5 = StudentForm(prefix="stu5")
    stu6 = StudentForm(prefix="stu6")
    if request.method == "POST":
        stu1 = StudentForm(request.POST, prefix="stu1")
        stu2 = StudentForm(request.POST, prefix="stu2")
        stu3 = StudentForm(request.POST, prefix="stu3")
        stu4 = StudentForm(request.POST, prefix="stu4")
        stu5 = StudentForm(request.POST, prefix="stu5")
        stu6 = StudentForm(request.POST, prefix="stu6")
        if stu1.is_valid() and stu2.is_valid() and stu3.is_valid() and stu4.is_valid():
            if(student_is.student_user==stu1.cleaned_data["student_user"]):
                if (Student.objects.filter(student_user=stu1.cleaned_data["student_user"]).exists() and
            Student.objects.filter(student_user=stu2.cleaned_data["student_user"]).exists()
            and Student.objects.filter(student_user=stu3.cleaned_data["student_user"]).exists()
            and Student.objects.filter(student_user=stu4.cleaned_data["student_user"]).exists()
            and Student.objects.filter(student_user=stu5.cleaned_data["student_user"]).exists()
            and Student.objects.filter(student_user=stu6.cleaned_data["student_user"]).exists()):
            
                    student1=Student.objects.get(student_user=stu1.cleaned_data["student_user"])
                    student2=Student.objects.get(student_user=stu2.cleaned_data["student_user"])
                    student3=Student.objects.get(student_user=stu3.cleaned_data["student_user"])
                    student4=Student.objects.get(student_user=stu4.cleaned_data["student_user"])
                    student5=Student.objects.get(student_user=stu5.cleaned_data["student_user"])
                    student6=Student.objects.get(student_user=stu6.cleaned_data["student_user"])

                    if (student1.admin_tick==True and student2.admin_tick==True and student3.admin_tick==True and student4.admin_tick==True
                    and student5.admin_tick==True and student6.admin_tick==True):
                        if(student1.in_group==False and student2.in_group==False and student3.in_group==False and student4.in_group==False
                        and student5.in_group==False and student6.in_group==False):

                            student1.end_day=stu1.cleaned_data["end_day"]
                            student2.end_day=stu2.cleaned_data["end_day"]
                            student3.end_day=stu3.cleaned_data["end_day"]
                            student4.end_day=stu4.cleaned_data["end_day"]
                            student5.end_day=stu5.cleaned_data["end_day"]
                            student6.end_day=stu6.cleaned_data["end_day"]

                            student1.start_day=stu1.cleaned_data["start_day"]
                            student2.start_day=stu2.cleaned_data["start_day"]
                            student3.start_day=stu3.cleaned_data["start_day"]
                            student4.start_day=stu4.cleaned_data["start_day"]
                            student5.start_day=stu5.cleaned_data["start_day"]
                            student6.start_day=stu6.cleaned_data["start_day"]

                            student1.in_group=True
                            student2.in_group=True
                            student3.in_group=True
                            student4.in_group=True
                            student5.in_group=True
                            student6.in_group=True

                            student1.save()
                            student2.save()
                            student3.save()
                            student4.save()
                            student5.save()
                            student6.save()

                            stu1.save()
                            stu2.save()
                            stu3.save()
                            stu4.save()
                            stu5.save()
                            stu6.save()
                        
                            StudentGroup6.objects.create(group_name=student1.student_user,stu1=student1,stu2=student2,stu3=student3,stu4=student4,stu5=student5,
                            stu6=student6,
                            stu1_tick=True,stu2_tick=False,stu3_tick=False,stu4_tick=False,stu5_tick=False,stu6_tick=False)
                            return JsonResponse({"success":"update informations."})
                        else:
                            return JsonResponse({"error":"the student already in Group"})

                    else:
                        return JsonResponse({"error":"admin_tick is False."})
            else:
                return JsonResponse({"error":"This user dont Login"})
        else:
            return JsonResponse({"error":"Invalid Data"})


    dicti={"stu1":stu1,"stu2":stu2,"stu3":stu3,"stu4":stu4,"stu5":stu5,"stu6":stu6}
    return render(request,'group6.html',dicti)

def my_group(request):
    student_id = request.session.get("student_id")
    student_is = Student.objects.get(id=student_id)
    if (StudentGroup3.objects.filter(stu1=student_is) ):

        mygroup3=StudentGroup3.objects.get(stu1=student_is)

        student1=mygroup3.stu1.student_user
        student2=mygroup3.stu2.student_user
        student3=mygroup3.stu3.student_user
        student1_tick=mygroup3.stu1_tick
        student2_tick=mygroup3.stu2_tick
        student3_tick=mygroup3.stu3_tick

        return render(request,"mygroup31.html",{"stu1":student1, "stu2":student2, "stu3":student3,
        "stu1_tick":student1_tick,"stu2_tick":student2_tick,"stu3_tick":student3_tick})

    elif (StudentGroup3.objects.filter(stu2=student_is) ):

        mygroup3=StudentGroup3.objects.get(stu2=student_is)

        student1=mygroup3.stu1.student_user
        student2=mygroup3.stu2.student_user
        student3=mygroup3.stu3.student_user
        student1_tick=mygroup3.stu1_tick
        student2_tick=mygroup3.stu2_tick
        student3_tick=mygroup3.stu3_tick

        return render(request,"mygroup31.html",{"stu1":student1, "stu2":student2, "stu3":student3,
        "stu1_tick":student1_tick,"stu2_tick":student2_tick,"stu3_tick":student3_tick})

    elif (StudentGroup3.objects.filter(stu3=student_is) ):

        mygroup3=StudentGroup3.objects.get(stu3=student_is)

        student1=mygroup3.stu1.student_user
        student2=mygroup3.stu2.student_user
        student3=mygroup3.stu3.student_user
        student1_tick=mygroup3.stu1_tick
        student2_tick=mygroup3.stu2_tick
        student3_tick=mygroup3.stu3_tick

        return render(request,"mygroup31.html",{"stu1":student1, "stu2":student2, "stu3":student3,
        "stu1_tick":student1_tick,"stu2_tick":student2_tick,"stu3_tick":student3_tick})

    elif (StudentGroup4.objects.filter(stu1=student_is) ):

        mygroup4=StudentGroup4.objects.get(stu1=student_is)

        student1=mygroup4.stu1.student_user
        student2=mygroup4.stu2.student_user
        student3=mygroup4.stu3.student_user
        student4=mygroup4.stu4.student_user
        student1_tick=mygroup4.stu1_tick
        student2_tick=mygroup4.stu2_tick
        student3_tick=mygroup4.stu3_tick
        student4_tick=mygroup4.stu4_tick

        return render(request,"mygroup41.html",{"stu1":student1, "stu2":student2, "stu3":student3,"stu4":student4,
        "stu1_tick":student1_tick,"stu2_tick":student2_tick,"stu3_tick":student3_tick,"stu4_tick":student4_tick})

    elif (StudentGroup4.objects.filter(stu2=student_is) ):

        mygroup4=StudentGroup4.objects.get(stu2=student_is)

        student1=mygroup4.stu1.student_user
        student2=mygroup4.stu2.student_user
        student3=mygroup4.stu3.student_user
        student4=mygroup4.stu4.student_user
        student1_tick=mygroup4.stu1_tick
        student2_tick=mygroup4.stu2_tick
        student3_tick=mygroup4.stu3_tick
        student4_tick=mygroup4.stu4_tick

        return render(request,"mygroup41.html",{"stu1":student1, "stu2":student2, "stu3":student3,"stu4":student4,
        "stu1_tick":student1_tick,"stu2_tick":student2_tick,"stu3_tick":student3_tick,"stu4_tick":student4_tick})

    elif (StudentGroup4.objects.filter(stu3=student_is) ):

        mygroup4=StudentGroup4.objects.get(stu3=student_is)

        student1=mygroup4.stu1.student_user
        student2=mygroup4.stu2.student_user
        student3=mygroup4.stu3.student_user
        student4=mygroup4.stu4.student_user
        student1_tick=mygroup4.stu1_tick
        student2_tick=mygroup4.stu2_tick
        student3_tick=mygroup4.stu3_tick
        student4_tick=mygroup4.stu4_tick
        return render(request,"mygroup41.html",{"stu1":student1, "stu2":student2, "stu3":student3,"stu4":student4,
        "stu1_tick":student1_tick,"stu2_tick":student2_tick,"stu3_tick":student3_tick,"stu4_tick":student4_tick})

    elif (StudentGroup4.objects.filter(stu4=student_is) ):

        mygroup4=StudentGroup4.objects.get(stu4=student_is)

        student1=mygroup4.stu1.student_user
        student2=mygroup4.stu2.student_user
        student3=mygroup4.stu3.student_user
        student4=mygroup4.stu4.student_user
        student1_tick=mygroup4.stu1_tick
        student2_tick=mygroup4.stu2_tick
        student3_tick=mygroup4.stu3_tick
        student4_tick=mygroup4.stu4_tick

        return render(request,"mygroup41.html",{"stu1":student1, "stu2":student2, "stu3":student3,"stu4":student4,
        "stu1_tick":student1_tick,"stu2_tick":student2_tick,"stu3_tick":student3_tick,"stu4_tick":student4_tick})

    elif (StudentGroup6.objects.filter(stu1=student_is) ):

        mygroup6=StudentGroup6.objects.get(stu1=student_is)

        student1=mygroup6.stu1.student_user
        student2=mygroup6.stu2.student_user
        student3=mygroup6.stu3.student_user
        student4=mygroup6.stu4.student_user
        student5=mygroup6.stu5.student_user
        student6=mygroup6.stu6.student_user
        student1_tick=mygroup6.stu1_tick
        student2_tick=mygroup6.stu2_tick
        student3_tick=mygroup6.stu3_tick
        student4_tick=mygroup6.stu4_tick
        student5_tick=mygroup6.stu6_tick
        student6_tick=mygroup6.stu6_tick

        return render(request,"mygroup61.html",{"stu1":student1, "stu2":student2, "stu3":student3,"stu4":student4,"stu5":student5,"stu6":student6,
        "stu1_tick":student1_tick,"stu2_tick":student2_tick,"stu3_tick":student3_tick ,"stu4_tick":student4_tick,"stu5_tick":student5_tick,"stu6_tick":student6_tick})
    elif (StudentGroup6.objects.filter(stu2=student_is) ):

        mygroup6=StudentGroup6.objects.get(stu2=student_is)

        student1=mygroup6.stu1.student_user
        student2=mygroup6.stu2.student_user
        student3=mygroup6.stu3.student_user
        student4=mygroup6.stu4.student_user
        student5=mygroup6.stu5.student_user
        student6=mygroup6.stu6.student_user
        student1_tick=mygroup6.stu1_tick
        student2_tick=mygroup6.stu2_tick
        student3_tick=mygroup6.stu3_tick
        student4_tick=mygroup6.stu4_tick
        student5_tick=mygroup6.stu6_tick
        student6_tick=mygroup6.stu6_tick

        return render(request,"mygroup61.html",{"stu1":student1, "stu2":student2, "stu3":student3,"stu4":student4,"stu5":student5,"stu6":student6,
        "stu1_tick":student1_tick,"stu2_tick":student2_tick,"stu3_tick":student3_tick ,"stu4_tick":student4_tick,"stu5_tick":student5_tick,"stu6_tick":student6_tick})

    elif (StudentGroup6.objects.filter(stu3=student_is) ):

        mygroup6=StudentGroup6.objects.get(stu3=student_is)

        student1=mygroup6.stu1.student_user
        student2=mygroup6.stu2.student_user
        student3=mygroup6.stu3.student_user
        student4=mygroup6.stu4.student_user
        student5=mygroup6.stu5.student_user
        student6=mygroup6.stu6.student_user
        student1_tick=mygroup6.stu1_tick
        student2_tick=mygroup6.stu2_tick
        student3_tick=mygroup6.stu3_tick
        student4_tick=mygroup6.stu4_tick
        student5_tick=mygroup6.stu6_tick
        student6_tick=mygroup6.stu6_tick

        return render(request,"mygroup61.html",{"stu1":student1, "stu2":student2, "stu3":student3,"stu4":student4,"stu5":student5,"stu6":student6,
        "stu1_tick":student1_tick,"stu2_tick":student2_tick,"stu3_tick":student3_tick ,"stu4_tick":student4_tick,"stu5_tick":student5_tick,"stu6_tick":student6_tick})

    elif (StudentGroup6.objects.filter(stu4=student_is) ):

        mygroup6=StudentGroup6.objects.get(stu4=student_is)

        student1=mygroup6.stu1.student_user
        student2=mygroup6.stu2.student_user
        student3=mygroup6.stu3.student_user
        student4=mygroup6.stu4.student_user
        student5=mygroup6.stu5.student_user
        student6=mygroup6.stu6.student_user
        student1_tick=mygroup6.stu1_tick
        student2_tick=mygroup6.stu2_tick
        student3_tick=mygroup6.stu3_tick
        student4_tick=mygroup6.stu4_tick
        student5_tick=mygroup6.stu6_tick
        student6_tick=mygroup6.stu6_tick

        return render(request,"mygroup61.html",{"stu1":student1, "stu2":student2, "stu3":student3,"stu4":student4,"stu5":student5,"stu6":student6,
        "stu1_tick":student1_tick,"stu2_tick":student2_tick,"stu3_tick":student3_tick ,"stu4_tick":student4_tick,"stu5_tick":student5_tick,"stu6_tick":student6_tick})

    elif (StudentGroup6.objects.filter(stu5=student_is) ):

        mygroup6=StudentGroup6.objects.get(stu5=student_is)

        student1=mygroup6.stu1.student_user
        student2=mygroup6.stu2.student_user
        student3=mygroup6.stu3.student_user
        student4=mygroup6.stu4.student_user
        student5=mygroup6.stu5.student_user
        student6=mygroup6.stu6.student_user
        student1_tick=mygroup6.stu1_tick
        student2_tick=mygroup6.stu2_tick
        student3_tick=mygroup6.stu3_tick
        student4_tick=mygroup6.stu4_tick
        student5_tick=mygroup6.stu6_tick
        student6_tick=mygroup6.stu6_tick

        return render(request,"mygroup61.html",{"stu1":student1, "stu2":student2, "stu3":student3,"stu4":student4,"stu5":student5,"stu6":student6,
        "stu1_tick":student1_tick,"stu2_tick":student2_tick,"stu3_tick":student3_tick ,"stu4_tick":student4_tick,"stu5_tick":student5_tick,"stu6_tick":student6_tick})

    elif (StudentGroup6.objects.filter(stu6=student_is) ):

        mygroup6=StudentGroup6.objects.get(stu6=student_is)

        student1=mygroup6.stu1.student_user
        student2=mygroup6.stu2.student_user
        student3=mygroup6.stu3.student_user
        student4=mygroup6.stu4.student_user
        student5=mygroup6.stu5.student_user
        student6=mygroup6.stu6.student_user
        student1_tick=mygroup6.stu1_tick
        student2_tick=mygroup6.stu2_tick
        student3_tick=mygroup6.stu3_tick
        student4_tick=mygroup6.stu4_tick
        student5_tick=mygroup6.stu6_tick
        student6_tick=mygroup6.stu6_tick

        return render(request,"mygroup61.html",{"stu1":student1, "stu2":student2, "stu3":student3,"stu4":student4,"stu5":student5,"stu6":student6,
        "stu1_tick":student1_tick,"stu2_tick":student2_tick,"stu3_tick":student3_tick ,"stu4_tick":student4_tick,"stu5_tick":student5_tick,"stu6_tick":student6_tick})
    else:
        return HttpResponse("You Dont Have A Group.")

from decimal import Decimal, InvalidOperation


def bill_count(end_day, start_day, price_per_day):
    if end_day and start_day:
        dayis = (end_day - start_day).days
        try:
            es = dayis * Decimal(price_per_day)
        except InvalidOperation:
            return Decimal("0")
        return es
    return Decimal("0")


def reserve(request):
    student_id = request.session.get("student_id")
    student_is = Student.objects.get(id=student_id)
    room_reserved = RoomForm()
    if request.method == "POST":
        room_reserved = RoomForm(request.POST)
        if StudentGroup3.objects.filter(group_name=student_is.student_user):
            g3 = StudentGroup3.objects.get(group_name=student_is.student_user)
            if g3.stu1_tick==False or g3.stu2_tick==False or g3.stu3_tick==False:
                return HttpRespone("User dont Accept")
            elif room_reserved.is_valid():
                cd = room_reserved.cleaned_data
                if Room.objects.filter(
                    block=cd["block"], room_number=cd["room_number"]
                ):
                    room = Room.objects.filter(
                        block=cd["block"], room_number=cd["room_number"]
                    )[0]
                    if room.capacity - room.num_of_people_in_room >= 3:
                        room.num_of_people_in_room += 3
                        room.group3 = g3

                        g3.stu1.room_is = room
                        g3.stu2.room_is = room
                        g3.stu3.room_is = room
                        g3.stu1.billing = bill_count(
                            g3.stu1.end_day, g3.stu1.start_day, room.price_per_day
                        )
                        g3.stu2.billing = bill_count(
                            g3.stu2.end_day, g3.stu2.start_day, room.price_per_day
                        )
                        g3.stu3.billing = bill_count(
                            g3.stu3.end_day, g3.stu3.start_day, room.price_per_day
                        )
                        g3.save()
                        g3.stu1.save()
                        g3.stu2.save()
                        g3.stu3.save()
                        room.save()
                    else:
                        return HttpResponse("Room is full.")
                else:
                    return HttpResponse("Room is full or not valid.")
            else:
                return HttpResponse("Form is not valid.")
        if StudentGroup4.objects.filter(group_name=student_is.student_user):
            g4 = StudentGroup4.objects.get(group_name=student_is.student_user)
            if g4.stu1_tick==False or g4.stu2_tick==False or g4.stu3_tick==False or g4.stu4_tick==False:
                return HttpRespone("User dont Accept")
            elif room_reserved.is_valid():
                cd = room_reserved.cleaned_data
                if Room.objects.filter(
                    block=cd["block"], room_number=cd["room_number"]
                ):
                    room = Room.objects.filter(
                        block=cd["block"], room_number=cd["room_number"]
                    )[0]
                    if room.capacity - room.num_of_people_in_room >= 4:
                        room.num_of_people_in_room += 4
                        room.group4 = g4
    ##change to while student change room so the last room should delete.
    
                        g4.stu1.room_is = room
                        g4.stu2.room_is = room
                        g4.stu3.room_is = room
                        g4.stu4.room_is = room

                        g4.stu1.billing = bill_count(
                            g4.stu1.end_day, g4.stu1.start_day, room.price_per_day
                        )
                        g4.stu2.billing = bill_count(
                            g4.stu2.end_day, g4.stu2.start_day, room.price_per_day
                        )
                        g4.stu3.billing = bill_count(
                            g4.stu3.end_day, g4.stu3.start_day, room.price_per_day
                        )
                        g4.stu4.billing = bill_count(
                            g4.stu4.end_day, g4.stu4.start_day, room.price_per_day
                        )
                        g4.save()
                        g4.stu1.save()
                        g4.stu2.save()
                        g4.stu3.save()
                        g4.stu4.save()
                        room.save()
                    else:
                        return HttpResponse("Room is full.")
                else:
                    return HttpResponse("Room is full or not valid.")
            else:
                return HttpResponse("Form is not valid.")
        else:
            return HttpResponse("You are not the head.")

        if StudentGroup6.objects.filter(group_name=student_is.student_user):
            g6 = StudentGroup6.objects.get(group_name=student_is.student_user)
            if (
                g6.stu1_tick == False
                or g6.stu2_tick == False
                or g6.stu3_tick == False
                or g6.stu4_tick == False
                or g6.stu5_tick == False
                or g6.stu6_tick == False
            ):
                return HttpRespone("User dont Accept")
            elif room_reserved.is_valid():
                cd = room_reserved.cleaned_data
                if Room.objects.filter(
                    block=cd["block"], room_number=cd["room_number"]
                ):
                    room = Room.objects.filter(
                        block=cd["block"], room_number=cd["room_number"]
                    )[0]
                    if room.capacity - room.num_of_people_in_room >= 6:
                        room.num_of_people_in_room += 6
                        room.group6 = g6

                        g6.stu1.room_is = room
                        g6.stu2.room_is = room
                        g6.stu3.room_is = room
                        g6.stu4.room_is = room
                        g6.stu5.room_is = room
                        g6.stu6.room_is = room

                        g6.stu1.billing = bill_count(
                            g6.stu1.end_day, g6.stu1.start_day, room.price_per_day
                        )
                        g6.stu2.billing = bill_count(
                            g6.stu2.end_day, g6.stu2.start_day, room.price_per_day
                        )
                        g6.stu3.billing = bill_count(
                            g6.stu3.end_day, g6.stu3.start_day, room.price_per_day
                        )
                        g6.stu4.billing = bill_count(
                            g6.stu4.end_day, g6.stu4.start_day, room.price_per_day
                        )
                        g6.stu5.billing = bill_count(
                            g6.stu5.end_day, g6.stu5.start_day, room.price_per_day
                        )
                        g6.stu6.billing = bill_count(
                            g6.stu6.end_day, g6.stu6.start_day, room.price_per_day
                        )
                        g6.save()
                        g6.stu1.save()
                        g6.stu2.save()
                        g6.stu3.save()
                        g6.stu4.save()
                        g6.stu5.save()
                        g6.stu6.save()
                        room.save()
                    else:
                        return HttpResponse("Room is full.")
                else:
                    return HttpResponse("Room is full or not valid.")
            else:
                return HttpResponse("Form is not valid.")
        else:
            return HttpResponse("You are not the head.")
    rooms = Room.objects.filter(num_of_people_in_room__lt=F('capacity'))

    return render(request, "reserve.html", {"room": room_reserved,"rooms":rooms})
