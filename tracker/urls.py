from django.urls import path

from . import views

urlpatterns = [
    path('', views.MeasurementListView.as_view(), name="tracker-home")
]
