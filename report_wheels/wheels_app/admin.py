from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *


class TravelReportsAdmin(admin.ModelAdmin):
    search_fields = [
        "id",
        "reporting_to",
        "travel_location",
        "department__name",
        "travel_vendor_name__name",
    ]


class DepartmentAdmin(admin.ModelAdmin):
    search_fields = ["name"]


class TravelVendorNameAdmin(admin.ModelAdmin):
    search_fields = ["name"]


admin.site.register(TravelReports, TravelReportsAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(TravelVendorName, TravelVendorNameAdmin)


# CHnage admin Panel
admin.site.site_header = "Reports Wheels Panel"
admin.site.site_title = "Reports Wheels Admin Panel"
admin.site.index_title = "Reports Wheels Administration"
admin.site.site_footer = "Designed and Developed by Ahmed Qureshi"
