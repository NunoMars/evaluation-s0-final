from django.contrib import admin
from .models import MajorArcana
from import_export.admin import ImportExportMixin

class TaskAdmin(ImportExportMixin, admin.ModelAdmin):
    pass

# Register your models here.
admin.site.register(MajorArcana, TaskAdmin)
fields = ["image_tag"]
readonly_fields = ["image_tag"]
