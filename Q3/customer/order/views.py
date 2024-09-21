from django.shortcuts import render
from .models import Order
from django.db.models import Sum
from django.utils import timezone
from datetime import timedelta
# Create your views here.

def customers_view(request):
    customers = Order.objects.all()
    return render(request, 'customers.html', {'customers': customers})

def tcustomers_view(request):
    six_months_ago = timezone.now() - timedelta(days=6 * 30)
    tcustomers = Order.objects.filter(order_date__gte=six_months_ago).values('customer').annotate(total_spent=Sum('total_amount')).order_by('-total_spent')[:5]
    return render(request, 'tcustomers.html', {'tcustomers': tcustomers})


