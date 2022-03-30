from django.contrib import admin

from .models import Measurement, UserGoals, UserMeasurementTypesVisibility

admin.site.register(Measurement)
admin.site.register(UserMeasurementTypesVisibility)
admin.site.register(UserGoals)
