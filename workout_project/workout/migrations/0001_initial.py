# Generated by Django 4.1 on 2022-09-06 14:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('week_name', models.CharField(max_length=50)),
                ('day_of_week', models.DateField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schedule_name', models.CharField(max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='schedules', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exercise_name', models.CharField(max_length=50)),
                ('weight', models.IntegerField()),
                ('set', models.IntegerField()),
                ('reps', models.IntegerField()),
                ('day', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exercises', to='workout.day')),
            ],
        ),
        migrations.AddField(
            model_name='day',
            name='schedule',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='days', to='workout.schedule'),
        ),
    ]
