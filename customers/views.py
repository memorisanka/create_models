from django.shortcuts import render
from .forms import CustomerForm


def produce_consumer(request):
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "customers/customer-add.html", {})
    else:
        form = CustomerForm()

    return render(request, "customers/home.html", {"form": form})
