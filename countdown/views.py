from pprint import pprint as print

from django.http import JsonResponse
from django.shortcuts import render
from django.utils.timezone import datetime, timedelta

from .models import Waqt


WAQT_NAME_DICT = {}
WAQT_NAME_DICT["fazr"] = "ফজর"
WAQT_NAME_DICT["juhr"] = "যোহর"
WAQT_NAME_DICT["asr"] = "আসর"
WAQT_NAME_DICT["magrib"] = "মাগরিব"
WAQT_NAME_DICT["isha"] = "ঈশা"
WAQT_NAME_DICT["chast"] = "চাশত"

BANGLA_NUMBERS = {'1'}


def get_time_from_seconds(sec):
    m, s = divmod(sec, 60)
    h, m = divmod(m, 60)
    # return "%d:%02d:%02d" % (h, m, s)
    return "{}:{}".format(int(h), int(m), int(s))


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


def get_current_waqt(now=None, city=None):
    if now is None:
        now = datetime.strptime(datetime.now().strftime("%H:%M %d-%m-%Y"), "%H:%M %d-%m-%Y") # + timedelta(hours=4)
    if city is None:
        city = "Dhaka"
    salat_waqt = Waqt.objects.get(month=now.month, day=now.day, city=city)
    print(salat_waqt)
    waqt_times = get_waqt_times(salat_waqt)

    if now >= waqt_times["fazr_start"] and now <= waqt_times["fazr_end"]:
        response = {
            "waqt": "fazr",
            "end_time": waqt_times["fazr_end"],
            'end_timestamp': waqt_times["fazr_end"].timestamp(),
            "current_time": now.strftime('%H:%M %d/%m/%Y'),
            "current_timestamp": now.timestamp(),
            "remaining_time": get_time_from_seconds(waqt_times["fazr_end"].timestamp() - now.timestamp()),
            "city": city,
        }

    elif now >= waqt_times["chast_start"] and now <= waqt_times["chast_end"]:
        response = {
            "waqt": "chast",
            "end_time": waqt_times["chast_end"],
            'end_timestamp': waqt_times["chast_end"].timestamp(),
            "current_time": now.strftime('%H:%M %d/%m/%Y'),
            "current_timestamp": now.timestamp(),
            "remaining_time": get_time_from_seconds(waqt_times["chast_end"].timestamp() - now.timestamp()),
            "city": city,
        }

    elif now >= waqt_times["juhr_start"] and now <= waqt_times["juhr_end"]:
        response = {
            "waqt": "juhr",
            "end_time": waqt_times["juhr_end"],
            'end_timestamp': waqt_times["juhr_end"].timestamp(),
            "current_time": now.strftime('%H:%M %d/%m/%Y'),
            "current_timestamp": now.timestamp(),
            "remaining_time": get_time_from_seconds(waqt_times["juhr_end"].timestamp() - now.timestamp()),
            "city": city,
        }

    elif now >= waqt_times["asr_start"] and now <= waqt_times["asr_end"]:
        response = {
            "waqt": "asr",
            "end_time": waqt_times["asr_end"],
            'end_timestamp': waqt_times["asr_end"].timestamp(),
            "current_time": now.strftime('%H:%M %d/%m/%Y'),
            "current_timestamp": now.timestamp(),
            "remaining_time": get_time_from_seconds(waqt_times["asr_end"].timestamp() - now.timestamp()),
            "city": city,
        }

    elif now >= waqt_times["magrib_start"]and now <= waqt_times["magrib_end"]:
        response = {
            "waqt": "magrib",
            "end_time": waqt_times["magrib_end"],
            'end_timestamp': waqt_times["magrib_end"].timestamp(),
            "current_time": now.strftime('%H:%M %d/%m/%Y'),
            "current_timestamp": now.timestamp(),
            "remaining_time": get_time_from_seconds(waqt_times["magrib_end"].timestamp() - now.timestamp()),
            "city": city,
        }

    elif now >= waqt_times["isha_start"] and now <= waqt_times["isha_end"]:
        response = {
            "waqt": "isha",
            "end_time": waqt_times["isha_end"],
            'end_timestamp': waqt_times["isha_end"].timestamp(),
            "current_time": now.strftime('%H:%M %d/%m/%Y'),
            "current_timestamp": now.timestamp(),
            "remaining_time": get_time_from_seconds(waqt_times["isha_end"].timestamp() - now.timestamp()),
            "city": city,
        }

    else:
        response = {
            "waqt": "unknown",
            "end_time": "unknown",
            'end_timestamp': "unknown",
            "current_time": now.strftime('%H:%M %d/%m/%Y'),
            "current_timestamp": now.timestamp(),
            "remaining_time": "unknown",
            "city": "unknown",
        }

    return response


def get_current_waqt_for_web(request):
    waqt_json = get_current_waqt()
    print(waqt_json["end_time"])

    context = {
        'waqt': WAQT_NAME_DICT.get(waqt_json["waqt"]),
        'end_time': waqt_json["end_time"],
        'city': waqt_json["city"],
    }
    return render(request, 'current_waqt.html', context)


def get_current_waqt_for_chatfuel(request):
    waqt_json = get_current_waqt()
    text_respones = "এখন {} এর সময়। শেষ হতে আর {}{} মিনিট বাকি আছে। আজকে {} এর শেষ সময় {} ।".format(
        WAQT_NAME_DICT.get(waqt_json["waqt"]),
        (waqt_json["remaining_time"].split(':')[0]+" ঘণ্টা ") if int(waqt_json["remaining_time"].split(':')[0]) else "",
        waqt_json["remaining_time"].split(':')[1],
        WAQT_NAME_DICT.get(waqt_json["waqt"]),
        waqt_json["end_time"].strftime('%I:%M %p')
    )

    response = {
        "messages": [
            {"text": text_respones}
        ]
    }

    return JsonResponse(response, status=200)

