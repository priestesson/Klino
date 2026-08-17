from django.urls import path
from .views import booking_page


urlpatterns = [
    path("bookings/", include("bookings.urls")),
]