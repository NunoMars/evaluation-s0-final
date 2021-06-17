from django.contrib import admin
from .models import MajorArcana

# Register your models here.
admin.site.register(MajorArcana)
fields = ['image_tag']
readonly_fields = ['image_tag']