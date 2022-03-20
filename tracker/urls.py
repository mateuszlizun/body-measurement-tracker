from django.urls import path

from . import views

app_name = "tracker"

urlpatterns = [
    path("", views.DashboardView.as_view(), name="home"),
    path("charts/", views.MeasurementChartView.as_view(), name="charts"),
    path("history/", views.MeasurementListView.as_view(), name="history"),
    path(
        "measurement/<int:pk>/",
        views.MeasurementDetailView.as_view(),
        name="measurement-detail",
    ),
]
