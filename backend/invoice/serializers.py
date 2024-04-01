from rest_framework import serializers
from models import *

class InvoiceItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoiceItem
        fields = '__all__'

class InvoiceBillSundrySerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoiceBillSundry
        fields = '__all__'

class InvoiceSerializer(serializers.ModelSerializer):
    items = InvoiceItemSerializer(many=True)
    bill_sundry = InvoiceBillSundrySerializer(many=True)

    class Meta:
        model = Invoice
        fields = '__all__'

    def validate(self, data):
        items_data = data.pop('items')
        bill_sundry_data = data.pop('bill_sundry')
        total_amount = 0

        for item in items_data:
            amount = item['quantity'] * item['price']
            if amount <= 0 or item['quantity'] <= 0 or item['price'] <= 0:
                raise serializers.ValidationError("Invalid amount, quantity, or price for item.")
            total_amount += amount

        for sundry in bill_sundry_data:
            if sundry['amount'] <= 0:
                raise serializers.ValidationError("Invalid amount for bill sundry.")

            total_amount += sundry['amount']

        if total_amount != data['total_amount']:
            raise serializers.ValidationError("Invalid Total amount.")

        return data



