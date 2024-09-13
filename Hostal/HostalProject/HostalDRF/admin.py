from django.contrib import admin
from .models import (
    Room,
    Student,
    StudentGroup3,
    StudentGroup4,
    StudentGroup6,
    ReserveStudent,
    Login,GroupStudent
)

# Register your models here.
admin.site.register(Room)
admin.site.register(Student)
admin.site.register(StudentGroup3)
admin.site.register(StudentGroup4)
admin.site.register(StudentGroup6)
admin.site.register(ReserveStudent)
admin.site.register(Login)
admin.site.register(GroupStudent)