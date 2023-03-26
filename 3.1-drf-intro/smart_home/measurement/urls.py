from django.urls import path
from .views import MeasurementsAPIViews, SensorAPIUpdateRetrieve, SensorAPIViews 

urlpatterns = [
    path('sensors/', SensorAPIViews.as_view()),
    path('measurements/', MeasurementsAPIViews.as_view()),
    path('sensors/<int:pk>/', SensorAPIUpdateRetrieve.as_view()),
]
