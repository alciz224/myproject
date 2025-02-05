from django.contrib import admin
from . models import Credential

@admin.register(Credential)
class CredentialAdmin(admin.ModelAdmin):
    list_display = ('name', 'code')
    search_fields = ('name', 'code')
