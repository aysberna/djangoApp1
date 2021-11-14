from django.shortcuts import render
from .models import NavigationRecord, Vehicle
from datetime import date, datetime, timedelta, timezone

# Create your views here.
def index(request):
    time_threshold = datetime.now() - timedelta(hours=48)
    navigationRecords = NavigationRecord.objects.filter(datetime__gte=time_threshold)
    print('======', navigationRecords.values())
    # for nr in navigationRecords.values():
    #     vehicle = Vehicle.objects.filter(id=nr['vehicle_id'])
    #     nr['vehicle_plate'] = vehicle
    return render(request, "index.html", {"navigationRecords": navigationRecords})

#   navigationRecords = NavigationRecord.objects.all()
#   return render(request, "index.html", {"navigationRecord": navigationRecords})
# def addNavigationRecord(request):
#     if request.method == "GET":
#         return redirect("/"
#     else:
#         datetime = request.POST.get("datetime")

#         newNavigationRecord = NavigationRecord(datetime = datetime)
#         newNavigationRecord.save()
#         return redirect("/")


