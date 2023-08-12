import json
from rest_framework.viewsets import ModelViewSet

from core.models import TransferOrder
from core.serializers import TransferOrderSerializer
from core.clients import AWSSQSClient


class TransferOrderViewSet(ModelViewSet):
    queryset = TransferOrder.objects.all()
    serializer_class = TransferOrderSerializer

    def create(self, request, *args, **kwargs):
        AWSSQSClient().send_message(json.dumps(request.data))
        return super().create(request, *args, **kwargs)
