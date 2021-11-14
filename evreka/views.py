from django.shortcuts import render
from .models import NavigationRecord, Vehicle
from datetime import date, datetime, timedelta, timezone

# Create your views here.
def index(request):
    time_threshold = datetime.now() - timedelta(hours=48)
    navigationRecords = NavigationRecord.objects.filter(datetime__gte=time_threshold)
    return render(request, "index.html", {"navigationRecords": navigationRecords})



