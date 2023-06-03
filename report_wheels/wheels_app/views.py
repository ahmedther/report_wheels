from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.core.paginator import Paginator

# Create your views here.

from wheels_app.decorators import check_auth_redirect
from wheels_app.models import TravelReports


@login_required(login_url="login_page")
def home(request):
    if request.method == "GET":
        page = {}
        travel_reports = TravelReports.objects.all().order_by("-id")
        print(travel_reports)
        # Create a paginator with 14 items per page
        paginator = Paginator(travel_reports, 14)

        # Get the requested page number from the query parameters
        page_number = request.GET.get("page") or 1
        page = paginator.page(page_number)

        return render(request, "wheels_app/home.html", {"page": page})


@check_auth_redirect
def login_page(request):
    context = {}
    if request.method == "GET":
        return render(request, "wheels_app/login_page.html", context)
    if request.method == "POST":
        print(request.POST)
        # Login User
        user = authenticate(
            request,
            username=request.POST["username"],
            password=request.POST["password"],
        )
        if user is None:
            context[
                "error"
            ] = "Wrong User ID or Password. Try again or call 33333 /33330 to reset it."
            return render(request, "wheels_app/login_page.html", context)
        if user:
            login(request, user)
            user_full_name = request.user.get_full_name()
            context = {"user_fullname": user_full_name}
            return redirect("home")
