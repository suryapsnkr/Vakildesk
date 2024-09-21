from django.urls import path
from .views import customers_view, tcustomers_view

urlpatterns = [
    path('customers/', customers_view, name='customers'),
    path('tcustomers/', tcustomers_view, name='tcustomers'),
]