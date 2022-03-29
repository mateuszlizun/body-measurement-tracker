from django.contrib import admin

from .models import Measurement, UserMeasurementTypesVisibility

admin.site.register(Measurement)
admin.site.register(UserMeasurementTypesVisibility)
