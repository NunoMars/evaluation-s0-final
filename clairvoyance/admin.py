from django.contrib import admin
from .models import MajorArcana
from import_export.admin import ImportExportMixin

class MajorArcanaAdmin(ImportExportMixin, MajorArcana):
    pass

# Register your models here.
admin.site.register(MajorArcana, ImportExportMixin)
fields = ["image_tag"]
readonly_fields = ["image_tag"]
