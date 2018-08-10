from django.contrib import admin
from . import models

# Register your models here.


class ClientInline(admin.StackedInline):
    model = models.Client
    extra = 0


class KidInline(admin.StackedInline):
    model = models.Child
    extra = 0


class DocInline(admin.StackedInline):
    model = models.Document
    extra = 0


class CaseAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'entry_date', 'was_recently_entered')
    list_filter = ['entry_date']
    search_fields = ['your_name', 'childs_name']
    inlines = [
        ClientInline,
        KidInline,
        DocInline,
    ]


admin.site.register(models.Case, CaseAdmin)

