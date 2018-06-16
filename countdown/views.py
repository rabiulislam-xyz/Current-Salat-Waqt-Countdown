import json
import requests

from pprint import pprint as print
from django.http import JsonResponse, HttpResponse
from django.utils.timezone import datetime, timedelta

from .models import Waqt


def get_time_from_seconds(sec):
    m, s = divmod(sec, 60)
    h, m = divmod(m, 60)
    return "%d:%02d:%02d" % (h, m, s)


def get_waqt_times(waqt):
    waqt_times = {
        "fazr_start":datetime.strptime("{} {}-{}-{}".format(waqt.fazr, waqt.day, waqt.month, waqt.year), "%H:%M %d-%m-%Y"),
        "fazr_end": datetime.strptime("{} {}-{}-{}".format(waqt.sunrise, waqt.day, waqt.month, waqt.year), "%H:%M %d-%m-%Y"),

        "chast_start": datetime.strptime("{} {}-{}-{}".format(waqt.sunrise, waqt.day, waqt.month, waqt.year), "%H:%M %d-%m-%Y"),
        "chast_end": datetime.strptime("{} {}-{}-{}".format(waqt.juhr, waqt.day, waqt.month, waqt.year), "%H:%M %d-%m-%Y"),

        "juhr_start": datetime.strptime("{} {}-{}-{}".format(waqt.juhr, waqt.day, waqt.month, waqt.year), "%H:%M %d-%m-%Y"),
        "juhr_end": datetime.strptime("{} {}-{}-{}".format(waqt.asr, waqt.day, waqt.month, waqt.year), "%H:%M %d-%m-%Y"),

        "asr_start": datetime.strptime("{} {}-{}-{}".format(waqt.asr, waqt.day, waqt.month, waqt.year), "%H:%M %d-%m-%Y"),
        "asr_end": datetime.strptime("{} {}-{}-{}".format(waqt.magrib, waqt.day, waqt.month, waqt.year), "%H:%M %d-%m-%Y"),

        "magrib_start": datetime.strptime("{} {}-{}-{}".format(waqt.magrib, waqt.day, waqt.month, waqt.year), "%H:%M %d-%m-%Y"),
        "magrib_end": datetime.strptime("{} {}-{}-{}".format(waqt.isha, waqt.day, waqt.month, waqt.year), "%H:%M %d-%m-%Y"),

        "isha_start": datetime.strptime("{} {}-{}-{}".format(waqt.isha, waqt.day, waqt.month, waqt.year), "%H:%M %d-%m-%Y"),
        "isha_end": datetime.strptime("{} {}-{}-{}".format(waqt.fazr, waqt.day, waqt.month, waqt.year), "%H:%M %d-%m-%Y") + timedelta(hours=24),
    }
    return waqt_times


def get_current_waqt(request):
    now = datetime.strptime(datetime.now().strftime("%H:%M %d-%m-%Y"), "%H:%M %d-%m-%Y") # + timedelta(hours=4)
    salat_waqt = Waqt.objects.get(month=now.month, day=now.day, city='Dhaka')
    print(salat_waqt)
    waqt_times = get_waqt_times(salat_waqt)

    # print("=================================================")
    # print('isha start ' + str(waqt_times["isha_start"]))
    # print('now '+ str(now))
    # print(now > waqt_times["isha_start"])
    # print(now < waqt_times["isha_end"])
    # print('isha end ' + str(waqt_times["isha_end"]))
    # print("=================================================")


    if now >= waqt_times["fazr_start"] and now <= waqt_times["fazr_end"]:
        response = {
            "waqt": "fazr",
            "end_time": waqt_times["fazr_end"].strftime('%H:%M %d/%m/%Y'),
            'end_timestamp': waqt_times["fazr_end"].timestamp(),
            "current_time": now.strftime('%H:%M %d/%m/%Y'),
            "current_timestamp": now.timestamp(),
        }
    elif now >= waqt_times["chast_start"] and now <= waqt_times["chast_end"]:
        response = {
            "waqt": "chast",
            "end_time": waqt_times["chast_end"].strftime('%H:%M %d/%m/%Y'),
            'end_timestamp': waqt_times["chast_end"].timestamp(),
            "current_time": now.strftime('%H:%M %d/%m/%Y'),
            "current_timestamp": now.timestamp(),
        }
    elif now >= waqt_times["juhr_start"] and now <= waqt_times["juhr_end"]:
        response = {
            "waqt": "juhr",
            "end_time": waqt_times["juhr_end"].strftime('%H:%M %d/%m/%Y'),
            'end_timestamp': waqt_times["juhr_end"].timestamp(),
            "current_time": now.strftime('%H:%M %d/%m/%Y'),
            "current_timestamp": now.timestamp(),
        }
    elif now >= waqt_times["asr_start"] and now <= waqt_times["asr_end"]:
        response = {
            "waqt": "asr",
            "end_time": waqt_times["asr_end"].strftime('%H:%M %d/%m/%Y'),
            'end_timestamp': waqt_times["asr_end"].timestamp(),
            "current_time": now.strftime('%H:%M %d/%m/%Y'),
            "current_timestamp": now.timestamp(),
        }
    elif now >= waqt_times["magrib_start"]and now <= waqt_times["magrib_end"]:
        response = {
            "waqt": "magrib",
            "end_time": waqt_times["magrib_end"].strftime('%H:%M %d/%m/%Y'),
            'end_timestamp': waqt_times["magrib_end"].timestamp(),
            "current_time": now.strftime('%H:%M %d/%m/%Y'),
            "current_timestamp": now.timestamp(),
        }
    elif now >= waqt_times["isha_start"] and now <= waqt_times["isha_end"]:
        response = {
            "waqt": "isha",
            "end_time": waqt_times["isha_end"].strftime('%H:%M %d/%m/%Y'),
            'end_timestamp': waqt_times["isha_end"].timestamp(),
            "current_time": now.strftime('%H:%M %d/%m/%Y'),
            "current_timestamp": now.timestamp(),
            "remaining_time": get_time_from_seconds(waqt_times["isha_end"].timestamp() - now.timestamp()),
        }
    else:
        response = {
            "waqt": "unknown",
            "status": "not ok",
            "current_time": now.strftime('%H:%M %d/%m/%Y'),
            "current_timestamp": now.timestamp(),
        }
        return JsonResponse(response, status=500)

    return JsonResponse(response, status=200)

