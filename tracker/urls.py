from django.urls import path

from . import views

app_name = "tracker"

urlpatterns = [
    path("", views.MeasurementListView.as_view(), name="home"),
    path("charts/", views.MeasurementChartView.as_view(), name="charts"),
]
