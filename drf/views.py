from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import DRF
from .serializers import DRFSerializer

class DRFList(ListCreateAPIView):
    queryset = DRF.objects.all()
    serializer_class = DRFSerializer

class DRFDetail(RetrieveUpdateDestroyAPIView):
    queryset = DRF.objects.all()
    serializer_class = DRFSerializer