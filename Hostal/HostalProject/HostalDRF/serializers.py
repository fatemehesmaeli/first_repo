from rest_framework import serializers
from .models import (Room,
Student,
StudentGroup3,
StudentGroup4,
StudentGroup6,
ReserveStudent,
Login)
from datetime import datetime


class StudentSerializer(serializers.ModelSerializer):
    room_is = serializers.StringRelatedField()

    def bill_count(self, student: Student):
        if student.end_day and student.start_day:
            dayis = (student.end_day - student.start_day).days
            es = (
                dayis * student.room_is.price_per_day
            ) 
            return str(es)
        return 0

    Bill = serializers.SerializerMethodField(method_name="bill_count")

    class Meta:
        model = Student
        fields = [
            "student_user",
            "student_password",
            "field",
            "room_is",
            "start_day",
            "end_day",
            "Bill",
            "admin_tick",
            "in_group",
            "stu_tick"
        ]


class StudentGroup3Serializer(serializers.ModelSerializer):
    stu1 = StudentSerializer()
    stu2 = StudentSerializer()
    stu3 = StudentSerializer()

    class Meta:
        model = StudentGroup3
        fields = ['group_name','stu1','stu2','stu3','stu1_tick','stu2_tick','stu3_tick']


class StudentGroup4Serializer(serializers.ModelSerializer):
    stu1 = StudentSerializer()
    stu2 = StudentSerializer()
    stu3 = StudentSerializer()
    stu4 = StudentSerializer()

    class Meta:
        model = StudentGroup4
        fields = fields = [
            "group_name",
            "stu1",
            "stu2",
            "stu3",
            'stu4',
            "stu1_tick",
            "stu2_tick",
            "stu3_tick",
            'stu4_tick'
        ]


class StudentGroup6Serializer(serializers.ModelSerializer):
    stu1 = StudentSerializer()
    stu2 = StudentSerializer()
    stu3 = StudentSerializer()
    stu4 = StudentSerializer()
    stu5 = StudentSerializer()
    stu6 = StudentSerializer()

    class Meta:
        model = StudentGroup6
        fields = fields = [
            "group_name",
            "stu1",
            "stu2",
            "stu3",
            "stu4",
            "stu5",
            "stu6",
            "stu1_tick",
            "stu2_tick",
            "stu3_tick",
            "stu4_tick",
            "stu5_tick",
            "stu6_tick",
        ]


class RoomSerializer(serializers.ModelSerializer):
    group3 = StudentGroup3Serializer()
    group4 = StudentGroup4Serializer()
    group6 = StudentGroup6Serializer()
    # def get_groups(self,product:Room):
    #     if Room.capacity == 3:
    #         self.group4 = None
    #         self.group6 = None
    #         if group3:
    #             return self.group3
    #     elif Room.capacity == 4:
    #         self.group3 = None
    #         self.group6 = None
    #         if group4:
    #             return self.group4
        
    #     else:
    #         self.group4 = None
    #         self.group3 = None
    #         if group6:
    #             return self.group6
    #         return None

    # actualgroup = serializers.SerializerMethodField(method_name='get_groups')


    class Meta:
        model = Room
        fields = [
            "block",
            "room_number",
            "capacity",
            "num_of_people_in_room",
            "price_per_day",
            # "actualgroup",
            'group3',
            'group4',
            'group6'
        ]


class ReserveStudentSerializer(serializers.ModelSerializer):
    group3 = StudentGroup3Serializer()
    group4 = StudentGroup4Serializer()
    group6 = StudentGroup6Serializer()
    room_reserve=RoomSerializer()
    # def get_groups(self,product:ReserveStudent):
    #     if ReserveStudent.NumberOfStudent == 3:
    #         self.group4 = None
    #         self.group6 = None
    #         return self.group3
    #     elif ReserveStudent.NumberOfStudent == 4:
    #         self.group3 = None
    #         self.group6 = None
    #         return self.group4

    #     else:
    #         self.group4 = None
    #         self.group3 = None
    #     return self.group6

    # actualgroup = serializers.SerializerMethodField(method_name='get_groups')

    class Meta:
        model = ReserveStudent
        fields = [
            "NumberOfStudent",
            # 'actualgroup'
            "group3",
            "group4",
            "group6",
            "room_reserve"
        ]

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model=Login
        fields=['password','username']
