from django.contrib import admin
from .models import MajorArcana
from import_export.admin import ImportExportActionModelAdmin

class MajorArcanaAdmin(ImportExportActionModelAdmin):
    pass

# Register your models here.
admin.site.register(MajorArcana)
fields = ["image_tag"]
readonly_fields = ["image_tag"]
