from django.db import models
import uuid

class Invoice(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date = models.DateTimeField()
    invoice_number = models.PositiveIntegerField(unique=True)
    customer_name = models.CharField(max_length=100)
    billing_address = models.CharField(max_length=255)
    shipping_address = models.CharField(max_length=255)
    GSTIN = models.CharField(max_length=15)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

class InvoiceItem(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    invoice = models.ForeignKey(Invoice, related_name='items', on_delete=models.CASCADE)
    item_name = models.CharField(max_length=100)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

class InvoiceBillSundry(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    invoice = models.ForeignKey(Invoice, related_name='bill_sundry', on_delete=models.CASCADE)
    bill_sundry_name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)








