import calendar
from datetime import datetime
from django.db import models


def get_current_year():
    return datetime.now().year


class Waqt(models.Model):
    city = models.CharField(max_length=127, default='Dhaka')
    day = models.IntegerField(help_text='unix format for day (%d)', null=True, blank=True)
    month = models.IntegerField(help_text='unix format for month (%m)', null=True, blank=True)
    year = models.IntegerField(help_text='unix format for month (%Y)', default=get_current_year)

    fazr = models.CharField(max_length=15, null=True, blank=True)
    sunrise = models.CharField(max_length=15, null=True, blank=True)
    juhr = models.CharField(max_length=15, null=True, blank=True)
    asr = models.CharField(max_length=15, null=True, blank=True)
    magrib = models.CharField(max_length=15, null=True, blank=True)
    isha = models.CharField(max_length=15, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} salat waqt for {} {}".format(self.city, self.day, calendar.month_name[self.month])

    class Meta:
        db_table = 'waqt'
        ordering = ['month', 'day']


# t='''
# 1	5:04	6:25	11:50	3:36	5:15	6:31
# 2	5:05	6:26	11:51	3:36	5:15	6:31
# 3	5:06	6:27	11:51	3:36	5:15	6:32
# 4	5:06	6:27	11:52	3:36	5:15	6:32
# 5	5:07	6:28	11:52	3:36	5:15	6:32
# 6	5:07	6:29	11:52	3:36	5:16	6:32
# 7	5:08	6:29	11:53	3:36	5:16	6:33
# 8	5:09	6:30	11:53	3:37	5:16	6:33
# 9	5:09	6:31	11:54	3:37	5:16	6:33
# 10	5:10	6:31	11:54	3:37	5:16	6:33
# 11	5:10	6:32	11:55	3:37	5:17	6:34
# 12	5:11	6:33	11:55	3:38	5:17	6:34
# 13	5:12	6:33	11:56	3:38	5:17	6:34
# 14	5:12	6:34	11:56	3:38	5:18	6:35
# 15	5:13	6:34	11:56	3:39	5:18	6:35
# 16	5:13	6:35	11:57	3:39	5:18	6:36
# 17	5:14	6:36	11:57	3:39	5:19	6:36
# 18	5:14	6:36	11:58	3:40	5:19	6:37
# 19	5:15	6:37	11:58	3:40	5:20	6:37
# 20	5:15	6:37	11:59	3:41	5:20	6:37
# 21	5:16	6:38	11:59	3:41	5:21	6:38
# 22	5:16	6:38	12:00	3:42	5:21	6:38
# 23	5:17	6:39	12:00	3:42	5:22	6:39
# 24	5:17	6:39	12:01	3:43	5:22	6:40
# 25	5:18	6:40	12:01	3:43	5:23	6:40
# 26	5:18	6:40	12:02	3:44	5:23	6:41
# 27	5:19	6:40	12:02	3:45	5:24	6:41
# 28	5:19	6:41	12:03	3:45	5:25	6:42
# 29	5:20	6:41	12:03	3:46	5:25	6:42
# 30	5:20	6:42	12:03	3:46	5:26	6:43
# 31	5:20	6:42	12:04	3:47	5:26	6:43
# '''.split('\n')
# def settime():
#     for line in t:
#         for i in line.split():
#             waqt, _ = Waqt.objects.get_or_create(month=12, day=line.split()[0], city='Dhaka')
#             waqt.fazr = line.split()[1]
#             waqt.sunrise = line.split()[2]
#             waqt.juhr = line.split()[3]
#
#             waqt.asr = datetime.strptime("{} PM".format(line.split()[4]), "%I:%M %p").strftime('%H:%M')
#             waqt.magrib = datetime.strptime("{} PM".format(line.split()[5]), "%I:%M %p").strftime('%H:%M')
#             waqt.isha = datetime.strptime("{} PM".format(line.split()[6]), "%I:%M %p").strftime('%H:%M')
#             waqt.save()
#             print(waqt)
