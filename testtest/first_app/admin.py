from django.contrib import admin
from .models import BFUser, AllABoldface, Minutes, OpsBriefMinutes, Absentee


class MinutesInLine(admin.TabularInline):
    model = Minutes


class MinutesAdmin(admin.ModelAdmin):
    model = Minutes
    list_display = [
        'who_talked',
        'write_up',
    ]


class OpsBriefMinutesAdmin(admin.ModelAdmin):
    inlines = [
        MinutesInLine,
    ]


# Register your models here.
admin.site.register(BFUser)
admin.site.register(AllABoldface)
admin.site.register(OpsBriefMinutes, OpsBriefMinutesAdmin)
admin.site.register(Absentee)