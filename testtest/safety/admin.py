from django.contrib import admin
from .models import SafetyAlertMsg, SafetyAlertMsgImages

# Register your models here.
class ImagesInLine(admin.TabularInline):
    model = SafetyAlertMsgImages


class ImagesAdmin(admin.ModelAdmin):
    model = SafetyAlertMsgImages
    list_display = ['image']


class SafetyAlertMsgAdmin(admin.ModelAdmin):
    inlines = [
        ImagesInLine,
    ]


admin.site.register(SafetyAlertMsgImages, ImagesAdmin)
admin.site.register(SafetyAlertMsg, SafetyAlertMsgAdmin)