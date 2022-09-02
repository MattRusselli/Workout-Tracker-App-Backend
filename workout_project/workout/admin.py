from django.contrib import admin
from .models import User, Schedule, Day, Exercise
# Register your models here.

admin.site.register(User)
admin.site.register(Schedule)
admin.site.register(Day)
admin.site.register(Exercise)
