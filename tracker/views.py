from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse

from .models import Measurement
from .forms import MeasurementCreateUpdateForm
from .constant import TRACKER_APP_NAME, HISTORY_PATH_NAME, MEASUREMENT_DETAIL_PATH_NAME


def get_path_name_with_namespace(path_name):
    return TRACKER_APP_NAME + ":" + path_name


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


class MeasurementCreateView(LoginRequiredMixin, CreateView):
    model = Measurement
    form_class = MeasurementCreateUpdateForm
    template_name = "tracker/measurement_create_form.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class MeasurementUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Measurement
    form_class = MeasurementCreateUpdateForm
    template_name = "tracker/measurement_update_form.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        measurement = self.get_object()
        return self.request.user == measurement.user

    def get_context_data(self, *args, **kwargs):
        context = super(MeasurementUpdateView, self).get_context_data(*args, **kwargs)

        history_url = get_path_name_with_namespace(HISTORY_PATH_NAME)

        if reverse(history_url) in self.request.META.get("HTTP_REFERER"):
            previous_url = history_url
        else:
            previous_url = get_path_name_with_namespace(MEASUREMENT_DETAIL_PATH_NAME)

        context["previous_url"] = previous_url

        return context
