from django.urls import path

from measurement.views import MeasurementsCreateView, SensorsRetrieveUpdateView, SensorsListCreateView

urlpatterns = [
    path('sensors/', SensorsListCreateView.as_view()),
    path('sensors/<pk>/', SensorsRetrieveUpdateView.as_view()),
    path('measurements/', MeasurementsCreateView.as_view()),
]
