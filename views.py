from django.shortcuts import render, redirect
from .models import Booking
# def success(request):
#     return render(request, "success.html")

def book_now(request):
    if request.method == "POST":
        # Get data from the form
        full_name = request.POST.get("name")
        email = request.POST.get("email")
        room_type = request.POST.get("room-type")
        move_in_date = request.POST.get("move-in-date")

        # Save the data to the database
        Booking.objects.create(
            full_name=full_name,
            email=email,
            room_type=room_type,
            move_in_date=move_in_date
        )

        # Redirect to a success page or show a success message
        return redirect("success")  # 'success' is a URL name we'll define below

    return render(request, "book_stay.html")

def success(request):
    return render(request, "success.html")
def home(request):
    return render(request,"index.html")



