from django.db import models
from django.contrib.auth.models import User

class Room(models.Model):
    # FIELDS = [
    #     ("Math", "Math"),
    #     ("Medical", "Medical"),
    #     # ("Guest", "Guest"),
    # ]
    block = models.IntegerField()
    room_number = models.IntegerField()
    capacity = models.IntegerField()
    num_of_people_in_room = models.IntegerField()
    price_per_day = models.DecimalField(max_digits=10, decimal_places=3)
    # room_field = models.CharField(max_length=100, choices=FIELDS)
    # groups = models.ForeignKey("Group", on_delete=models.CASCADE, null=True, blank=True)
    # if FIELDS == "Math" or FIELDS == "Medical":
    group3 = models.ForeignKey(
        "StudentGroup3", on_delete=models.CASCADE, null=True, blank=True
    )
    group4 = models.ForeignKey(
        "StudentGroup4", on_delete=models.CASCADE, null=True, blank=True
    )
    group6 = models.ForeignKey(
        "StudentGroup6", on_delete=models.CASCADE, null=True, blank=True
    )

    def save(self, *args, **kwargs):
        if self.capacity == 3:
            self.group4 = None
            self.group6 = None
        elif self.capacity == 4:
            self.group3 = None
            self.group6 = None
        elif self.capacity == 6:
            self.group3 = None
            self.group4 = None
        super().save(*args, **kwargs)

    # else:
    #     roups = models.ForeignKey(Guest, on_delete=callable)

class Student(models.Model):
    FIELDS = [
        ("Math", "Math"),
        ("Medical", "Medical"),
        # ("Guest", "Guest"),
    ]
    student_user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    field = models.CharField(max_length=100, choices=FIELDS,null=True)
    room_is = models.ForeignKey(Room, on_delete=models.CASCADE,null=True)
    start_day = models.DateTimeField()
    end_day = models.DateTimeField()
    billing = models.DecimalField(max_digits=10, decimal_places=3)
    admin_tick = models.BooleanField(default=False)

# first we dant have this option thi add last.
# class Guest(models.Model):
# guest_user = models.ForeignKey(User, on_delete=models.CASCADE)
# num_of_guest = models.IntegerField()
# start_day = models.DateTimeField()
# end_day = models.DateTimeField()
# room_is = models.ForeignKey(Room, on_delete=models.CASCADE)
# billing = models.DecimalField(max_digits=10, decimal_places=3)
# admin_tick = models.BooleanField(default=False)


# # class Admin(models.Model):
#     admin_user = models.ForeignKey(User, on_delete=models.CASCADE)


# class EmptyRoom(models.Model):
#     room = models.ForeignKey(Room, on_delete=models.CASCADE)


# class FullRoom(models.Model):
#     room = models.ForeignKey(Room, on_delete=models.CASCADE)


class StudentGroup3(models.Model):
    group_name = models.CharField(max_length=200)
    stu1 = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="stu1",null=True)
    stu2 = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="stu2",null=True)
    stu3 = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="stu3",null=True)


class StudentGroup4(models.Model):
    group_name = models.CharField(max_length=200)
    stu1 = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name="stu14", null=True
    )
    stu2 = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name="stu24", null=True
    )
    stu3 = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name="stu34", null=True
    )
    stu4 = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name="stu44", null=True
    )


class StudentGroup6(models.Model):
    group_name = models.CharField(max_length=200)
    stu1 = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name="stu16", null=True
    )
    stu2 = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name="stu26", null=True
    )
    stu3 = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name="stu36", null=True
    )
    stu4 = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name="stu46", null=True
    )
    stu5 = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name="stu56", null=True
    )
    stu6 = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name="stu66", null=True
    )

class ReserveStudent(models.Model):
    NumberOfStudent = models.IntegerField()
    group3 = models.ForeignKey(
        "StudentGroup3", on_delete=models.CASCADE, null=True, blank=True
    )
    group4 = models.ForeignKey(
        "StudentGroup4", on_delete=models.CASCADE, null=True, blank=True
    )
    group6 = models.ForeignKey(
        "StudentGroup6", on_delete=models.CASCADE, null=True, blank=True
    )

    def save(self, *args, **kwargs):
        if self.NumberOfStudent == 3:
            self.group4 = None
            self.group6 = None
        elif self.NumberOfStudent == 4:
            self.group3 = None
            self.group6 = None
        elif self.NumberOfStudent == 6:
            self.group3 = None
            self.group4 = None
        super().save(*args, **kwargs)
