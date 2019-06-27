from django.shortcuts import render, get_object_or_404,redirect
from accounts.models import Users,Device
<<<<<<< HEAD
from .models import DeviceList 
from django.utils import timezone
from django.conf import settings
import json
# Seungtae's part

from django.http import HttpResponse, JsonResponse

=======
from .models import DeviceList
from django.utils import timezone
from django.conf import settings    
import time
from datetime import datetime
>>>>>>> d3048589bbb18c0ac439bb6300820249fb2d4e17
def main(request):
    pass

def macList(request):
#     userId = 3
    if request.method == 'POST':
        userId = request.POST['pk']
        qs = Device.objects.filter(user_name=userId)
        return render(request, 'wifi/MAC.html', {
            'qs': qs
<<<<<<< HEAD
    })

def deviceCount (request):
        timequeryset = DeviceList.objects.all()
        data = [{'sniff_time': md.sniff_time, 'device_count': md.device_count} for md in timequeryset]
        return JsonResponse(data[-1], safe=False)
=======
        })
    return render(request, 'wifi/MAC.html', {
        })

def getDate(reqeust):
        macList =[]
        dateList = []
        if reqeust.method == 'POST':
                mac = reqeust.POST['macAddr']
                t1 = reqeust.POST['t1']
                t2 = reqeust.POST['t2']

                qs = DeviceList.objects.all()
                # t1 = 1561593600.0
                # t2 = 1561594500.0
                # mac = 'a4:d9:31:5f:26:99'

                for idx, val in enumerate(qs):
                        t = val.sniff_time.timestamp()
                        if t >= t1 and t <=t2:
                                macList.append(val.mac_list.split(","))
                for idx, val in enumerate(macList):
                        if mac in val:
                                dateList.append(qs[idx].sniff_time) 

        return render(reqeust, 'wifi/date.html', {
                'qs': dateList
        })

def getMacHour(request):
        dic = {}
        output = {}
        dateList = []
        toString = ''
        if request.method == 'POST':
                mac = request.POST['macAddr']
                # mac = 'a8:2b:b9:f0:52:94'
                qs = DeviceList.objects.all().order_by('sniff_time')
                for q in qs:
                        if mac in q.mac_list:
                                toString += str(q.sniff_time.year)
                                toString += str(q.sniff_time.month)
                                toString += str(q.sniff_time.day)
                                if toString not in dateList:
                                        dateList.append(toString)
                                        dic[toString] = []
                                        output[toString] = 0
                                dic[toString].append(q.sniff_time)
                                toString = ''

                for date in dateList:
                        leng = len(dic[date])
                        i = 0
                        while i < leng-1:
                                v1 = dic[date][i].hour*60 + dic[date][i].minute
                                v2 = dic[date][i+1].hour*60 + dic[date][i+1].minute
                                if v2 - v1 <= 5:
                                        output[date] += 5
                                elif i+2 is not leng:
                                        v2 = dic[date][i+2].hour*60 + dic[date][i+2].minute
                                        if v2 - v1 <= 10:
                                                output[date] += 10
                                        i+=1
                                        
        return render(request, 'wifi/date.html', {
               'qs': output
        })

>>>>>>> d3048589bbb18c0ac439bb6300820249fb2d4e17
