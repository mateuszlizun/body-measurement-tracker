from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse, reverse_lazy

from .models import Measurement, UserGoals, UserMeasurementTypesVisibility
from .forms import (
    MeasurementCreateUpdateForm,
    UserGoalsForm,
    UserMeasurementTypesVisibilityUpdateForm,
)
from .constant import (
    HOME_PATH_NAME,
    TRACKER_APP_NAME,
    HISTORY_PATH_NAME,
    MEASUREMENT_DETAIL_PATH_NAME,
)


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
                for name, v_name, value in Measurement.get_value_fields(measurement):
                    current_value = getattr(measurement, name)
                    previous_value = getattr(measurements[index + 1], name)

                    if current_value and previous_value:
                        setattr(
                            measurement,
                            name + "_difference",
                            current_value - previous_value,
                        )
        return measurements

    def get_context_data(self, *args, **kwargs):
        context = super(MeasurementListView, self).get_context_data(*args, **kwargs)

        context[
            "measurement_types_visibility"
        ] = UserMeasurementTypesVisibility.objects.get(user=self.request.user)

        return context


class DashboardView(LoginRequiredMixin, ListView):
    model = Measurement
    template_name = "tracker/dashboard.html"

    def get_queryset(self):
        return Measurement.objects.filter(user=self.request.user,).order_by(
            "pub_date"
        )[:10]

    def get_context_data(self, *args, **kwargs):
        context = super(DashboardView, self).get_context_data(*args, **kwargs)

        try:
            context["summary_data"] = Measurement.objects.filter(
                user=self.request.user
            ).latest("pub_date")

            latestMeasurements = Measurement.objects.filter(
                user=self.request.user
            ).order_by("-pub_date")[:5]

            userGoals = UserGoals.objects.get(user=self.request.user)

            if len(latestMeasurements) and userGoals:
                goals = []

                for name, v_name, value in UserGoals.get_value_fields(userGoals):
                    measurementValue = getattr(latestMeasurements[0], name)
                    if measurementValue:
                        if value >= measurementValue:
                            goals.append((name, v_name, 100))
                        else:
                            goals.append(
                                (
                                    name,
                                    v_name,
                                    round(
                                        ((measurementValue - value) / measurementValue)
                                        * 100
                                    ),
                                )
                            )

            context["latest_measurements"] = latestMeasurements
            context["user_goals"] = goals

        except Measurement.DoesNotExist:
            context["summary_data"] = None
            context["latest_measurements"] = None
            context["user_goals"] = None

        context[
            "measurement_types_visibility"
        ] = UserMeasurementTypesVisibility.objects.get(user=self.request.user)

        return context


class MeasurementDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Measurement

    def test_func(self):
        measurement = self.get_object()
        return self.request.user == measurement.user

    def get_context_data(self, *args, **kwargs):
        context = super(MeasurementDetailView, self).get_context_data(*args, **kwargs)

        context[
            "measurement_types_visibility"
        ] = UserMeasurementTypesVisibility.objects.get(user=self.request.user)

        return context


class MeasurementCreateView(LoginRequiredMixin, CreateView):
    model = Measurement
    form_class = MeasurementCreateUpdateForm
    template_name = "tracker/measurement_create_form.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()

        measurementsTypesVisibility = UserMeasurementTypesVisibility.objects.get(
            user=self.request.user
        )
        kwargs.update({"measurement_types_visibility": measurementsTypesVisibility})

        return kwargs


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

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()

        measurementsTypesVisibility = UserMeasurementTypesVisibility.objects.get(
            user=self.request.user
        )
        kwargs.update({"measurement_types_visibility": measurementsTypesVisibility})

        return kwargs


class MeasurementDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Measurement
    success_url = reverse_lazy(get_path_name_with_namespace(HISTORY_PATH_NAME))

    def test_func(self):
        measurement = self.get_object()
        return self.request.user == measurement.user

    def get_context_data(self, *args, **kwargs):
        context = super(MeasurementDeleteView, self).get_context_data(*args, **kwargs)

        history_url = get_path_name_with_namespace(HISTORY_PATH_NAME)

        if reverse(history_url) in self.request.META.get("HTTP_REFERER"):
            previous_url = history_url
        else:
            previous_url = get_path_name_with_namespace(MEASUREMENT_DETAIL_PATH_NAME)

        context["previous_url"] = previous_url

        return context


class UserMeasurementTypesVisibilityUpdateView(
    LoginRequiredMixin, UserPassesTestMixin, UpdateView
):
    model = UserMeasurementTypesVisibility
    form_class = UserMeasurementTypesVisibilityUpdateForm
    template_name = "tracker/user_measurement_types_visibility_update_form.html"
    success_url = reverse_lazy(get_path_name_with_namespace(HOME_PATH_NAME))

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        userMeasurementTypeVisibility = self.get_object()
        return self.request.user == userMeasurementTypeVisibility.user

    def get_object(self):
        return UserMeasurementTypesVisibility.objects.get(user=self.request.user)


class UserGoalsUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = UserGoals
    form_class = UserGoalsForm
    template_name = "tracker/user_goals_update_form.html"
    success_url = reverse_lazy(get_path_name_with_namespace(HOME_PATH_NAME))

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        userGoals = self.get_object()
        return self.request.user == userGoals.user

    def get_object(self):
        return UserGoals.objects.get(user=self.request.user)
