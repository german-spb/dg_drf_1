from rest_framework.viewsets import ModelViewSet
from .models import Sensor, Measurement
from .serializers import SensorSerializer, MeasurementSerializer, SensorDetailSerializer


class SensorViewSet(ModelViewSet):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class MeasurementViewSet(ModelViewSet):
    queryset = Measurement.objects.all()
    serializer_class = SensorDetailSerializer
