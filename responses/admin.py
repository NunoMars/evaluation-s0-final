from django.contrib import admin

from .models import (
    ResponsesBookPt,
    ResponsesBookEn,
    ResponsesBookEs,
    ResponsesBookFr,
)
from import_export.admin import ImportExportMixin


class TaskAdmin(ImportExportMixin, admin.ModelAdmin):
    pass


admin.site.register(ResponsesBookPt, TaskAdmin)
admin.site.register(ResponsesBookFr, TaskAdmin)
admin.site.register(ResponsesBookEn, TaskAdmin)
admin.site.register(ResponsesBookEs, TaskAdmin)
