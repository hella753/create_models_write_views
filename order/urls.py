from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("<int:order_id>/", views.individual_order, name="individual_order"),
]
