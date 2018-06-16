from django.contrib import admin

from countdown.models import Waqt


@admin.register(Waqt)
class WaqtAdmin(admin.ModelAdmin):
    list_filter = ('month', 'city', 'day', 'year')