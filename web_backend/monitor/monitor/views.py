import psutil as ps
import time
from django.http import JsonResponse
import os
import gzip
import re
import requests
import json


def cpu_memory_info(request):
    cpu = ps.cpu_count()
    names = []
    for i in range(cpu):
        names.append("CPU" + str(i + 1))
    names.append("Memory")
    percent = ps.cpu_percent(interval=1, percpu=True)
    percent.append(ps.virtual_memory().percent)
    return JsonResponse({
        "name": names,
        "percent": percent
    })


def cpu_info(request):
    cpu = ps.cpu_count()
    names = []
    for i in range(cpu):
        names.append("CPU" + str(i + 1))
    percent = ps.cpu_percent(interval=1, percpu=True)
    return JsonResponse({
        "name": names,
        "percent": percent
    })


def memory_info(request):
    memory = ps.virtual_memory()
    return JsonResponse({
        "name": "Memory",
        "memory_percent": memory.percent,
        "memory_available": round(memory.available / 1024 / 1024, 2),
        "memory_used": round(memory.used / 1024 / 1024, 2),
        "memory_total": round(memory.total / 1024 / 1024, 2)
    })


def net_disk_io(request):
    net_before = ps.net_io_counters()
    disk_before = ps.disk_io_counters()
    time.sleep(1.0)
    net_after = ps.net_io_counters()
    disk_after = ps.disk_io_counters()
    t = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    return JsonResponse({
        "net": {
            "sent": [
                t,
                round((net_after.bytes_sent - net_before.bytes_sent) / 1024, 2)
            ],
            "recv": [
                t,
                round((net_after.bytes_recv - net_before.bytes_recv) / 1024, 2)
            ]
        },
        "disk": {
            "write": [
                t,
                round((disk_after.write_bytes - disk_before.write_bytes) / 1024, 2)
            ],
            "read": [
                t,
                round((disk_after.read_bytes - disk_before.read_bytes) / 1024, 2)
            ]
        }

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


def log_analyze(request):
    INPUT_DIR = "static/logs"
    lineformat = re.compile(
        r"""(?P<ipaddress>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - - \[(?P<dateandtime>\d{2}\/[a-z]{3}\/\d{4}:\d{2}:\d{2}:\d{2} (\+|\-)\d{4})\] ((\"(GET|POST) )(?P<url>.+)(http\/1\.1")) (?P<statuscode>\d{3}) (?P<bytessent>\d+) (["](?P<refferer>(\-)|(.+))["]) (["](?P<useragent>.+)["])""",
        re.IGNORECASE)
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
    resp = [["count", "ip"]]
    for res in result:
        resp.append([result[res], str(res)])

    return JsonResponse({
        "resp": resp
    })


def battery_percent(request):
    def secs2hours(secs):
        mm, ss = divmod(secs, 60)
        hh, mm = divmod(mm, 60)
        return "%d:%02d:%02d" % (hh, mm, ss)
    battery = ps.sensors_battery()
    if battery.power_plugged:
        return JsonResponse({
            "percent": battery.percent
        })
    else:
        return JsonResponse({
            "percent": battery.percent,
            "secsleft": secs2hours(battery.secsleft)
        })


