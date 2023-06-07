from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from wheels_app.models import TravelReports, Department, TravelVendorName
from django.db.models import Q


class Helper:
    def __init__(self):
        pass

    def paginator(self, request, context, paginate_name="travel_objects"):
        page = request.GET.get("page")
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
        print(request.GET)

        fields = {
            "guest-name": "reporting_to",
            "flight-details": "flight_train_details",
            "pickup-location": "reporting_location",
            "drop-location": "travel_location",
            "travel-date": "travel_date",
            "reporting-time": "reporting_time",
            "vehicle-type": "vehicle_type",
            "booked-by": "vehicle_booked_by",
            "department": "department",
            "event-type": "event_type",
            "vendor-name": "travel_vendor_name",
            "bill-no": "bill_no",
            "bill-date": "bill_date",
            "bill-amount": "bill_amount",
            "note": "note",
        }

        if edit:
            travel_report = context["edit_obj"]
        else:
            travel_report = TravelReports()

        for field, attribute in fields.items():
            value = request.GET[field] or None
            if value:
                print(value)
                if field == "department":
                    value = Department.objects.get(id=value)
                elif field == "vendor-name":
                    value = TravelVendorName.objects.get(id=value)
                setattr(travel_report, attribute, value)

        travel_report.created_by = request.user
        travel_report.save()

        context["message"] = "✔ Success!"
        context[
            "message_inner"
        ] = f"A New Field for {travel_report} was added successfully"

        if edit:
            context[
                "message_inner"
            ] = f"Changes made to {travel_report} were successful"

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

