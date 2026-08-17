from django.shortcuts import render


def booking_page(request):
    return render(request, "bookings/booking.html")