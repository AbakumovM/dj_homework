from django.shortcuts import get_object_or_404
from .serializers import MeasurementSerializer, SensorDetailSerializer, SensorSerializer
from .models import Measurement, Sensor
from rest_framework import generics

class SensorAPIViews(generics.ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

class SensorAPIUpdateRetrieve(generics.RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


class MeasurementsAPIViews(generics.ListCreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

    def perform_create(self, serializer):
        sensor = get_object_or_404(Sensor, id=self.request.data.get('sensor'))
        return serializer.save(sensor=sensor)
