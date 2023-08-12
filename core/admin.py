from django.contrib import admin

from core.models import TransferOrder


@admin.register(TransferOrder)
class TransferOrderAdmin(admin.ModelAdmin):
    pass
