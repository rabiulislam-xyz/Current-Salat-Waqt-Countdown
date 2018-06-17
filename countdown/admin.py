from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from countdown.models import Waqt


@admin.register(Waqt)
class WaqtAdmin(ImportExportModelAdmin):
    list_filter = ('month', 'city', 'day', 'year')