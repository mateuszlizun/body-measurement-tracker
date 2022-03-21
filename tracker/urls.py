from django.urls import path

from . import views
from .constant import (
    TRACKER_APP_NAME,
    HISTORY_PATH_NAME,
    HOME_PATH_NAME,
    MEASUREMENT_DETAIL_PATH_NAME,
    MEASUREMENT_CREATE_PATH_NAME,
)

app_name = TRACKER_APP_NAME

urlpatterns = [
    path("", views.DashboardView.as_view(), name=HOME_PATH_NAME),
    path("charts/", views.MeasurementChartView.as_view(), name="charts"),
    path("history/", views.MeasurementListView.as_view(), name=HISTORY_PATH_NAME),
    path(
        "measurement/<int:pk>/",
        views.MeasurementDetailView.as_view(),
        name=MEASUREMENT_DETAIL_PATH_NAME,
    ),
    path(
        "measurement/new/",
        views.MeasurementCreateView.as_view(),
        name=MEASUREMENT_CREATE_PATH_NAME,
    ),
]
