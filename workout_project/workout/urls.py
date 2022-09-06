from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('users/', views.UserList.as_view(), name='user_list'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name='user_detail'),

    path('schedules/', views.ScheduleList.as_view(), name='schedule_list'),
    path('schedules/<int:pk>/', views.ScheduleDetail.as_view(),
         name='schedule_detail'),

    path('days/', views.DayList.as_view(), name='day_list'),
    path('days/<int:pk>/', views.DayDetail.as_view(), name='day_detail'),

    path('exercises/', views.ExerciseList.as_view(), name='exercise_list'),
    path('exercises/<int:pk>/', views.ExerciseDetail.as_view(),
         name='exercise_detail'),

    path("api/signup/", views.CreateUserView.as_view()),
]
