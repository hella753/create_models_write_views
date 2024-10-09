from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("<int:category_id>/", views.category, name="category"),
    path("product/", views.products, name="products"),
    path("product/<int:product_id>/", views.product, name="product"),
]
