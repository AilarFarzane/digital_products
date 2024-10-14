from django.urls import path

from digital_products.urls import urlpatterns
from .views import GatewayView, PaymentView

urlpatterns = [
    path('gateways/', GatewayView.as_view(), name='gateway'),
    path('pay/', PaymentView.as_view(), name='payments'),

]
