from django.db import models
class Room(models.Model):
    block = models.IntegerField()
    room_number = models.IntegerField()
    capacity = models.IntegerField()
    num_of_people_in_room = models.IntegerField()
    price_per_day = models.DecimalField(max_digits=10, decimal_places=3)
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
    def __str__(self):
        return f"{self.block} room{self.room_number}"

class Student(models.Model):
    FIELDS = [
        ("Math", "Math"),
        ("Medical", "Medical"),
    ]
    student_user =models.CharField(max_length=200,unique=True,null=True)
    student_password = models.CharField(max_length=200,unique=True,null=True)
    field = models.CharField(max_length=100, choices=FIELDS,null=True)
    room_is = models.ForeignKey(Room, on_delete=models.CASCADE,blank=True,null=True)
    start_day = models.DateField(blank=True,null=True)
    end_day = models.DateField(blank=True,null=True)
    billing = models.DecimalField(max_digits=10, decimal_places=3,blank=True,null=True)
    admin_tick = models.BooleanField(default=False)
    in_group = models.BooleanField(default=False)
    stu_tick=models.BooleanField(default=False)
    def __str__(self):
        return self.student_user

class GroupStudent(models.Model):
    FIELDS = [
        ("Math", "Math"),
        ("Medical", "Medical"),
    ]
    student_user = models.CharField(max_length=200,unique=True,null=True)
    field = models.CharField(max_length=100, choices=FIELDS, null=True)
    start_day = models.DateField(blank=True, null=True)
    end_day = models.DateField(blank=True, null=True)
class StudentGroup3(models.Model):
    group_name = models.CharField(max_length=200)
    stu1 = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="stu1",null=True
    )
    stu2 = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="stu2",null=True
    )
    stu3 = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="stu3",null=True
    )
    stu1_tick = models.BooleanField(default=False)
    stu2_tick = models.BooleanField(default=False)
    stu3_tick = models.BooleanField(default=False)

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
    stu1_tick = models.BooleanField(default=False)
    stu2_tick = models.BooleanField(default=False)
    stu3_tick = models.BooleanField(default=False)
    stu4_tick = models.BooleanField(default=False)

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
    stu1_tick = models.BooleanField(default=False)
    stu2_tick = models.BooleanField(default=False)
    stu3_tick = models.BooleanField(default=False)
    stu4_tick = models.BooleanField(default=False)
    stu5_tick = models.BooleanField(default=False)
    stu6_tick = models.BooleanField(default=False)


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
    room_reserve = models.ForeignKey(Room, on_delete=models.CASCADE, null=True)
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

class Login(models.Model):
    username = models.CharField(max_length=200)
    password=models.CharField(max_length=200)
