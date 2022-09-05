from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Schedule, Day, Exercise

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True),
    schedules = serializers.HyperlinkedRelatedField(
        view_name='schedule_detail',
        many=True,
        read_only=True)

    def create(self, validated_data):
        """
        Create and return a new User instance, given the validated data.
        """
        # make sure to user create_user method and not create
        # the later will not know how to hash the password properly
        user = User.objects.create_user(
            email=validated_data['email'],
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            password=validated_data['password'],
        )
        return user

    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'first_name',
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
