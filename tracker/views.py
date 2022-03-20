from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models import Measurement


class MeasurementListView(LoginRequiredMixin, ListView):
    model = Measurement

    def get_queryset(self):
        measurements = Measurement.objects.filter(user=self.request.user).order_by(
            "-pub_date"
        )

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


class MeasurementChartView(LoginRequiredMixin, ListView):
    model = Measurement
    template_name = "tracker/charts.html"

    def get_queryset(self):
        return Measurement.objects.filter(user=self.request.user).order_by("-pub_date")


class DashboardView(LoginRequiredMixin, ListView):
    model = Measurement
    template_name = "tracker/dashboard.html"

    def get_queryset(self):
        return Measurement.objects.filter(user=self.request.user).order_by("pub_date")

    def get_context_data(self, *args, **kwargs):
        context = super(DashboardView, self).get_context_data(*args, **kwargs)

        try:
            context["summary_data"] = Measurement.objects.filter(
                user=self.request.user
            ).latest("pub_date")
            context["latest_measurements"] = Measurement.objects.filter(
                user=self.request.user
            ).order_by("-pub_date")[:5]
        except Measurement.DoesNotExist:
            context["summary_data"] = None
            context["latest_measurements"] = None

        return context


class MeasurementDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Measurement

    def test_func(self):
        measurement = self.get_object()
        return self.request.user == measurement.user
