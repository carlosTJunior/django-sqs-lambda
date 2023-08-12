from django.db import models


class TransferOrder(models.Model):
    """A simplified model to represent a transfer of money or something countable"""

    amount = models.DecimalField(decimal_places=2, max_digits=19)
    sender_account = models.IntegerField()
    receiver_account = models.IntegerField()
    transaction_hash = models.UUIDField(primary_key=True)
