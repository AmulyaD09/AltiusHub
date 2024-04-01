from django.urls import path
from .views import *

urlpatterns = [
    path('invoices/', InvoiceListView.as_view(), name='invoice-list'),
    path('invoice/',InvoiceCreateView.as_view(),name='invoice-list-create'),
    path('invoice/<uuid:pk>/',InvoiceRetrieveUpdateDestroyView.as_view(),name='invoice-retrieve-update-delete'),
]