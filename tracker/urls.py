from django.urls import path

from . import views
from .constant import (
    TRACKER_APP_NAME,
    HISTORY_PATH_NAME,
    HOME_PATH_NAME,
    MEASUREMENT_DETAIL_PATH_NAME,
    MEASUREMENT_CREATE_PATH_NAME,
    MEASUREMENT_UPDATE_PATH_NAME,
    MEASUREMENT_DELETE_PATH_NAME,
    USER_MEASUREMENT_TYPES_PATH_NAME,
    USER_GOALS_PATH_NAME,
)

app_name = TRACKER_APP_NAME

urlpatterns = [
    path("", views.DashboardView.as_view(), name=HOME_PATH_NAME),
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
    path(
        "measurement/<int:pk>/update/",
        views.MeasurementUpdateView.as_view(),
        name=MEASUREMENT_UPDATE_PATH_NAME,
    ),
    path(
        "measurement/<int:pk>/delete/",
        views.MeasurementDeleteView.as_view(),
        name=MEASUREMENT_DELETE_PATH_NAME,
    ),
    path(
        "visibility-settings/",
        views.UserMeasurementTypesVisibilityUpdateView.as_view(),
        name=USER_MEASUREMENT_TYPES_PATH_NAME,
    ),
    path(
        "goals-settings/",
        views.UserGoalsUpdateView.as_view(),
        name=USER_GOALS_PATH_NAME,
    ),
]
