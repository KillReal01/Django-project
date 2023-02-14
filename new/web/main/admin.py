from django.contrib import admin
from .models import *


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('surname', 'name', 'patronymic', 'post', 'emp_date', 'salary')
    readonly_fields = ('photo_preview',)

    def photo_preview(self, obj):
        return obj.photo_preview

    photo_preview.short_description = 'Photo preview'
    photo_preview.allow_tags = True


admin.site.register(Employee, EmployeeAdmin)
