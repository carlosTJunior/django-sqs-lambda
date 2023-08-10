from rest_framework.viewsets import ModelViewSet

from core.models import TransferOrder
from core.serializers import TransferOrderSerializer


class TransferOrderViewSet(ModelViewSet):
    queryset = TransferOrder.objects.all()
    serializer_class = TransferOrderSerializer
