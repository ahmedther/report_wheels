from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from wheels_app.models import TravelReports, Department, TravelVendorName
from django.db.models import Q
from decimal import Decimal


class Helper:
    def __init__(self):
        pass

    def paginator(self, request, context, paginate_name="travel_objects"):
        page = request.GET.get("page")
        print(page)
        # results = 14
        results = 16
        paginator = Paginator(context[paginate_name], results)
        # context["paginator"] = paginator

        if not page:
            page = 1
        left_index = int(page) - 4
        if left_index < 1:
            left_index = 1

        right_index = int(page) + 5
        if right_index > paginator.num_pages:
            right_index = paginator.num_pages + 1

        custom_page_range = range(left_index, right_index)
        context["custom_page_range"] = custom_page_range
        try:
            context[paginate_name] = paginator.page(page)
        except PageNotAnInteger:
            page = 1
            context[paginate_name] = paginator.page(page)
        except EmptyPage:
            page = paginator.num_pages
            context[paginate_name] = paginator.page(page)

        return context

    def get_context(self, request, context):
        context["travel_objects"] = TravelReports.objects.all().order_by("-id")
        context["department_objects"] = Department.objects.all().order_by("-name")
        context["travel_vendor_objects"] = TravelVendorName.objects.all().order_by(
            "-name"
        )

        context["user_fullname"] = f"{request.user.get_full_name()} - ({request.user})"
        return context

    def post_new_report(self, request, context, edit=False):
        guest_name = request.GET.get("guest-name")
        flight_details = request.GET.get("flight-details")
        pickup_location = request.GET.get("pickup-location")
        drop_location = request.GET.get("drop-location")
        travel_date = request.GET.get("travel-date")
        reporting_time = request.GET.get("reporting-time")
        vehicle_type = request.GET.get("vehicle-type")
        booked_by = request.GET.get("booked-by")
        department_id = request.GET.get("department")
        if department_id:
            department_id = Department.objects.get(id=department_id)
        event_type = request.GET.get("event-type")
        travel_vendor_id = request.GET.get("vendor-name")
        if travel_vendor_id:
            travel_vendor_id = TravelVendorName.objects.get(id=travel_vendor_id)
        bill_no = request.GET.get("bill-no")
        bill_date = request.GET.get("bill-date")
        bill_amount = request.GET.get("bill-amount")
        note = request.GET.get("note")

        # Create a new TravelReports instance and set the field values
        if edit:
            travel_report = context["edit_obj"]
        else:
            travel_report = TravelReports()
        travel_report.reporting_to = guest_name
        travel_report.flight_train_details = flight_details
        travel_report.reporting_location = pickup_location
        travel_report.travel_location = drop_location
        travel_report.travel_date = travel_date
        travel_report.reporting_time = reporting_time
        travel_report.vehicle_type = vehicle_type
        travel_report.vehicle_booked_by = booked_by
        travel_report.department = department_id
        travel_report.event_type = event_type
        travel_report.travel_vendor_name = travel_vendor_id
        travel_report.bill_no = bill_no
        travel_report.bill_date = bill_date
        travel_report.bill_amount = bill_amount
        travel_report.note = note
        travel_report.created_by = request.user

        # Save the travel report
        travel_report.save()
        context["message"] = "✔ Success!"
        context[
            "message_inner"
        ] = f"A New Field for {travel_report} was Added successfully"  # Replace 'message_inner' with the URL or view name of your success page
        if edit:
            context["message_inner"] = f"Changes made {travel_report} was successful"
        return context

    def post_add_dept(self, request, context):
        new_dept_name = request.GET.get("new_dept_name")
        if new_dept_name:
            dept_obj = Department(name=new_dept_name)
            dept_obj.save()
            context["message"] = "✔ Success!"
            context[
                "message_inner"
            ] = f"A New Department {dept_obj} was Added successfully"
        return context

    def post_add_travel_vendor(self, request, context):
        new_travel_vendor = request.GET.get("new_travel_vendor")
        if new_travel_vendor:
            travel_obj = TravelVendorName(name=new_travel_vendor)
            travel_obj.save()
            context["message"] = "✔ Success!"
            context[
                "message_inner"
            ] = f"A Travel Vendor {travel_obj} was Added successfully"
        return context

    def process_search_request(self, request, search_query, context):
        context["page_href"] = f"search={search_query}"
        context.update(self.get_context(request, context))
        query = (
            Q(id__icontains=search_query)
            | Q(reporting_to=search_query)
            | Q(flight_train_details=search_query)
            | Q(reporting_location=search_query)
            | Q(travel_location=search_query)
            | Q(travel_date__icontains=search_query)
            | Q(vehicle_booked_by=search_query)
            | Q(department__name__icontains=search_query)
            | Q(travel_vendor_name__name__icontains=search_query)
            | Q(bill_no=search_query)
            | Q(bill_date__icontains=search_query)
        )
        if isinstance(search_query, float):
            query |= Q(bill_amount=search_query)
        context["travel_objects"] = (
            TravelReports.objects.distinct().filter(query).order_by("-id")
        )
        return context

    def get_object_with_id(self, pk_id, context):
        context["edit_obj"] = TravelReports.objects.get(id=pk_id)
        return context
