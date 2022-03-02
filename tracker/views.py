from django.views import generic
from django.contrib.auth.models import User

from .models import Measurement


class MeasurementListView(generic.ListView):
    model = Measurement

    def get_queryset(self):
        # TODO: logged in user ID should be retrieved here
        measurements = Measurement.objects.filter(user=User.objects.get(pk=1))

        for index, measurement in enumerate(measurements):
            if index != len(measurements) - 1:
                if measurement.chest and measurements[index + 1].chest:
                    measurement.chest_difference = (
                        measurement.chest - measurements[index + 1].chest
                    )
                if measurement.waist and measurements[index + 1].waist:
                    measurement.waist_difference = (
                        measurement.waist - measurements[index + 1].waist
                    )
                if measurement.hips and measurements[index + 1].hips:
                    measurement.hips_difference = (
                        measurement.hips - measurements[index + 1].hips
                    )
                if measurement.weight and measurements[index + 1].weight:
                    measurement.weight_difference = (
                        measurement.weight - measurements[index + 1].weight
                    )
        return measurements
