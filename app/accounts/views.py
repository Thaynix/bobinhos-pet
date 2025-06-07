from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .forms import AccountCreateForm


def register(request):
    """Register a new user account"""

    template_name = "register.html"
    context = {}

    if request.method == "POST":
        form = AccountCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")

    if request.method == "GET":
        form = AccountCreateForm()

    context["form"] = form
    return render(request, template_name, context)
