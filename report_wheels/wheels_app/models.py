from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Department(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class TravelVendorName(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class TravelReports(models.Model):
    reporting_to = models.CharField(max_length=255, blank=True, null=True)
    flight_train_details = models.CharField(max_length=255, blank=True, null=True)
    reporting_location = models.CharField(max_length=255, blank=True, null=True)
    travel_location = models.CharField(max_length=255, blank=True, null=True)
    travel_date = models.DateTimeField(blank=True, null=True)
    reporting_time = models.DateTimeField(blank=True, null=True)
    vehicle_type = models.CharField(max_length=255, blank=True, null=True)
    vehicle_booked_by = models.CharField(max_length=255, null=True)
    department = models.ForeignKey(
        Department,
        on_delete=models.SET_NULL,
        null=True,
        related_name="travel_reports_department",
        blank=True,
    )
    event_type = models.CharField(max_length=255, blank=True, null=True)
    travel_vendor_name = models.ForeignKey(
        TravelVendorName,
        on_delete=models.SET_NULL,
        null=True,
        related_name="travel_reports_vendor_name",
        blank=True,
    )
    bill_no = models.CharField(max_length=255, null=True)
    bill_date = models.DateTimeField(blank=True, null=True)
    bill_amount = models.DecimalField(
        max_digits=20, decimal_places=3, blank=True, null=True
    )
    note = models.TextField(blank=True, null=True)
    created_date = models.DateTimeField(
        auto_now=True, verbose_name="Creation Date", blank=True, null=True
    )
    created_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name="travel_reports_created_by",
        null=True,
    )

    def __str__(self):
        return f"{self.id} - {self.reporting_to} - {self.reporting_location}"
