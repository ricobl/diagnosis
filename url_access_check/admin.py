from django.contrib import admin
from models import URL, Fail

class URLAdmin(admin.ModelAdmin):
    list_display = ("address", "access_type")
    search_fields = ("address", "access_type")


class FailAdmin(admin.ModelAdmin):

    list_display    = ("url", "test_type", "user", "http_x_forwarded_for", "remote_addr", "when")
    search_fields   = ("url__address","test_type", "user", "http_x_forwarded_for", "remote_addr", "group_list", "user_agent")
    list_filter     = ("url", "test_type", "user", "http_x_forwarded_for", "remote_addr", "when")
    readonly_fields = ("url", "test_type", "user", "group_list", "http_x_forwarded_for", "remote_addr", "user_agent", "when")

    def has_add_permission(self, request):
        return False


admin.site.register(URL, URLAdmin)
admin.site.register(Fail, FailAdmin)