from django.shortcuts import render
from rest_framework import generics
from .serializers import UserSerializer, ScheduleSerializer, DaySerializer, ExerciseSerializer
from .models import User, Schedule, Day, Exercise

# Create your views here.


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ScheduleList(generics.ListCreateAPIView):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer


class ScheduleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer


class DayList(generics.ListCreateAPIView):
    queryset = Day.objects.all()
    serializer_class = DaySerializer


class DayDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Day.objects.all()
    serializer_class = DaySerializer


class ExerciseList(generics.ListCreateAPIView):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer


class ExerciseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
