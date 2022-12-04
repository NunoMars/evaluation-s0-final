from django.contrib import admin
from .models import SentencesFr, SentencesPt, SentencesEn, SentencesEs
from import_export.admin import ImportExportMixin


class TaskAdmin(ImportExportMixin, admin.ModelAdmin):
    pass


# Register your models here.
admin.site.register(SentencesFr, TaskAdmin)
admin.site.register(SentencesEs, TaskAdmin)
admin.site.register(SentencesEn, TaskAdmin)
admin.site.register(SentencesPt, TaskAdmin)
