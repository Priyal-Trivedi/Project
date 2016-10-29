
from django.contrib import admin
from models import *


class DefinitionsAdmin(admin.ModelAdmin):
    """

    """

    list_display = ('name', 'definition')
    list_filter = ('domain', 'tbl_scope')
    fieldsets = (
        (None, {'fields':('name', 'definition')}),
        ('Link', {'fields': ('link',)}),
        ('TBL Scope', {'fields': ('tbl_scope',)}),
        ('Domain', {'fields': ('domain',)}),
        ('Remarks', {'fields': ('remarks',)}))

    search_fields = ('name','domain', 'tbl_scope')


admin.site.register(Definitions, DefinitionsAdmin)
admin.site.register(Domain)
admin.site.register(TBL_Scope)