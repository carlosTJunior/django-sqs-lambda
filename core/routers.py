from rest_framework.routers import DefaultRouter

from core.viewsets import TransferOrderViewSet

router = DefaultRouter()
router.register("transfer-orders", TransferOrderViewSet)
