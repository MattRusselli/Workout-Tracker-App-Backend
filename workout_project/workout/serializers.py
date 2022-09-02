from rest_framework import serializers
from .models import User, Schedule, Day, Exercise


class UserSerializer(serializers.HyperlinkedModelSerializer):
    schedules = serializers.HyperlinkedRelatedField(
        view_name='schedule_detail',
        many=True,
        read_only=True)

    class Meta:
        model = User
        fields = ('id', 'email', 'first_name',
                  'last_name', 'password', 'schedules')


class ScheduleSerializer(serializers.HyperlinkedModelSerializer):
    days = serializers.HyperlinkedRelatedField(
        view_name='day_detail',
        many=True,
        read_only=True)

    class Meta:
        model = Schedule
        fields = ('id', 'schedule_name', 'days')


class DaySerializer(serializers.HyperlinkedModelSerializer):
    exercises = serializers.HyperlinkedRelatedField(
        view_name='exercise_detail',
        many=True,
        read_only=True)

    class Meta:
        model = Day
        fields = ('id', 'week_name', 'day_of_week', 'exercises')


class ExerciseSerializer(serializers.HyperlinkedModelSerializer):
    days = serializers.HyperlinkedRelatedField(
        view_name='day_detail',
        read_only=True)

    class Meta:
        model = Exercise
        fields = ('id', 'exercise_name', 'weight', 'set', 'reps', 'days')
