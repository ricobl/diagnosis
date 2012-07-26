from django.contrib import admin
from models import URL

class URLAdmin(admin.ModelAdmin):
    list_display = ("address", "access_type")
    search_fields = ("address", "access_type")

admin.site.register(URL, URLAdmin)