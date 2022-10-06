from django.contrib import admin
from .models import Sentences
from import_export.admin import ImportExportMixin
class TaskAdmin(ImportExportMixin, admin.ModelAdmin):
    pass
# Register your models here.
admin.site.register(Sentences, TaskAdmin)
