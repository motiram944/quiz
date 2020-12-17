from django.contrib import admin
from .models import Quiz

from import_export.admin import ImportExportModelAdmin

# admin.site.register(Quiz)

@admin.register(Quiz)
class ViewAdmin(ImportExportModelAdmin):
    pass