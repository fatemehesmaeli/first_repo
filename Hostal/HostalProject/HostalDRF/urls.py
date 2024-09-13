from django.urls import path
from . import views
from . import student_views
from . import admin_views
urlpatterns = [
    path("index/", views.index),
    # admin..
    path("students/", admin_views.StudentView.as_view()),
    path("students/<int:pk>/", admin_views.SingleStudentView.as_view()),
    path("Rooms/", admin_views.RoomView.as_view()),
    path("Rooms/<int:pk>/", admin_views.SingleRoomView.as_view()),
    path("reserves/", admin_views.ReserveStudentView.as_view()),
    path("reserves/<int:pk>/", admin_views.SingleReserveStudentView.as_view()),
    path("groups3/", admin_views.StudentGroup3View.as_view()),
    path("groups3/<int:pk>/", admin_views.SingleStudentGroup3View.as_view()),
    path("groups4/", admin_views.StudentGroup4View.as_view()),
    path("groups4/<int:pk>/", admin_views.SingleStudentGroup4View.as_view()),
    path("groups6/", admin_views.StudentGroup6View.as_view()),
    path("groups6/<int:pk>/", admin_views.SingleStudentGroup6View.as_view()),
    path("Logins/", admin_views.LoginView.as_view()),
    path("Logins/<int:pk>", admin_views.SingleLoginView.as_view()),
    # .....
    path("login/", student_views.log_in),
    path("get_querysets/", student_views.get_querysets, name="get_querysets"),
    path("group3/",student_views.group3),
    path("group4/",student_views.group4),
    path("group6/",student_views.group6),
    path("my_group/",student_views.my_group),
    path("reserve/",student_views.reserve),
]
