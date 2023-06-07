from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.core.paginator import Paginator

# Create your views here.

from wheels_app.decorators import check_auth_redirect
from wheels_app.v_helper import Helper


@login_required(login_url="login_page")
def home(request):
    context = {}
    try:
        if request.method == "GET":
            helper = Helper()
            new_report = request.GET.get("new_report")
            if new_report:
                context = helper.post_new_report(request, context)
            add_dept = request.GET.get("add_dept")
            if add_dept:
                context = helper.post_add_dept(request, context)
            add_travel_vendor = request.GET.get("add_travel_vendor")
            if add_travel_vendor:
                context = helper.post_add_travel_vendor(request, context)

            pk_id = request.GET.get("id")
            if pk_id:
                context = helper.get_object_with_id(pk_id, context)
            edit_page = request.GET.get("edit_page")
            if edit_page:
                context = helper.get_object_with_id(edit_page, context)
                context = helper.post_new_report(request, context, edit=True)
            search_query = request.GET.get("search")
            if search_query:
                context = helper.process_search_request(request, search_query, context)
                context = helper.paginator(request, context)
                return render(request, "wheels_app/home.html", context)
            context = helper.get_context(request, context)
            context = helper.paginator(request, context)

            return render(request, "wheels_app/home.html", context)
    except Exception as e:
        context["message"] = "❌ Error --  Failed!!! ❌ "
        context["message_inner"] = f"An Erorr has occured. Error :  {e}"
        return render(request, "wheels_app/home.html", context)


@check_auth_redirect
def login_page(request):
    context = {}
    if request.method == "GET":
        return render(request, "wheels_app/login_page.html", context)
    if request.method == "POST":
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


@login_required(login_url="login_page")
def logout_user(request):
    logout(request)
    return redirect("login_page")
