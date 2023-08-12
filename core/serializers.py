from rest_framework.serializers import ModelSerializer

from core.models import TransferOrder


class TransferOrderSerializer(ModelSerializer):
    class Meta:
        model = TransferOrder
        fields = "__all__"
