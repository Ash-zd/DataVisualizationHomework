import psutil as ps
import time
from django.http import HttpResponse, JsonResponse
import os
import sys
import gzip
import re
import requests
import json


def cpu_count(request):
    return JsonResponse({"cpu_count": ps.cpu_count()})


def cpu_percent(request):
    return JsonResponse({"cpu_percent": ps.cpu_percent(interval=1, percpu=True)})


def net_io(request):
    net_before = ps.net_io_counters()
    time.sleep(1.0)
    net_after = ps.net_io_counters()
    t = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    return JsonResponse({
        "sent": [
            t,
            round((net_after.bytes_sent - net_before.bytes_sent) / 1024, 2)
        ],
        "recv": [
            t,
            round((net_after.bytes_recv - net_before.bytes_recv) / 1024, 2)
        ]
    })


def net_analyze(request):
    INPUT_DIR = "static/logs"
    lineformat = re.compile(r"""(?P<ipaddress>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - - \[(?P<dateandtime>\d{2}\/[a-z]{3}\/\d{4}:\d{2}:\d{2}:\d{2} (\+|\-)\d{4})\] ((\"(GET|POST) )(?P<url>.+)(http\/1\.1")) (?P<statuscode>\d{3}) (?P<bytessent>\d+) (["](?P<refferer>(\-)|(.+))["]) (["](?P<useragent>.+)["])""", re.IGNORECASE)
    dictlist = []

    for f in os.listdir(INPUT_DIR):
        if f.endswith(".gz"):
            logfile = gzip.open(os.path.join(INPUT_DIR, f))
        else:
            logfile = open(os.path.join(INPUT_DIR, f))

        for l in logfile.readlines():
            data = re.search(lineformat, l)
            if data:
                datadict = data.groupdict()
                dictlist.append(datadict)
        logfile.close()
        ip = []
        for i in dictlist:
            ip.append(i["ipaddress"])
        result = {}
        for s in set(ip):
            result[s] = ip.count(s)
        # print(result.keys())
        # r = requests.get(url='http://ip.taobao.com/service/getIpInfo.php?ip=' + '118.89.29.54')
        # j = json.loads(r.content.decode('UTF-8'))
        # print(j["data"]["city"])

        result1 = result.copy()

        for r in result.keys():
            res = requests.get(url='http://ip.taobao.com/service/getIpInfo.php?ip=' + str(r))
            # j = json.loads(res.content.decode('UTF-8'))
            # print(j["data"]["city"])
            if res.status_code == 200:
                j = json.loads(res.content.decode("UTF-8"))
                result1[j["data"]["city"]] = result1.pop(str(r))

    # return JsonResponse({"dict": dictlist})
    resp = []
    print(result1)
    for r1 in result1.keys():
        resp.append({
            "name": str(r1),
            "value": result1[r1]
        })
    return JsonResponse({"resp": resp})



