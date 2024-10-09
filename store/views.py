from django.http import JsonResponse
from .models import Category, Product
from django.db.models import Max


def index(request):
    categories = Category.objects.all()
    categories_dictionary = {}
    categories_list = []
    for each_category in categories:
        categories_dictionary["კატეგორიის ID"] = each_category.id
        categories_dictionary["კატეგორია"] = each_category.category_name
        categories_dictionary["კატეგორიის აღწერა"] = (
            each_category.category_description
        )
        parent = each_category.parent_category
        if parent:
            categories_dictionary["ზეკატეგორიის ID"] = parent.id
            categories_dictionary["ზეკატეგორია"] = parent.category_name

        categories_list.append(categories_dictionary)
        categories_dictionary = {}
    return JsonResponse(
        categories_list,
        safe=False,
        json_dumps_params={'ensure_ascii': False}
    )


def products(request):
    products_elements = Product.objects.all()
    products_dictionary = {}
    products_list = []
    for product_element in products_elements:
        products_dictionary["პროდუქტის ID"] = product_element.id
        products_dictionary["პროდუქტის სახელი"] = product_element.product_name
        products_dictionary["პროდუქტის ფასი"] = product_element.product_price
        products_dictionary["პროდუქტის აღწერა"] = (
            product_element.product_description
        )
        max_cat = product_element.product_category.all().aggregate(Max("id"))
        cat = (
            product_element
            .product_category
            .all()
            .filter(id=max_cat['id__max'])
        )
        products_dictionary["პროდუქტის კატეგორია"] = (
            cat
            .first()
            .category_name
        )
        products_list.append(products_dictionary)
        products_dictionary = {}
    return JsonResponse(
        products_list,
        safe=False,
        json_dumps_params={'ensure_ascii': False}
    )


def category(request, category_id):
    category_element = Category.objects.get(id=category_id)
    categories_dictionary = {
        "კატეგორია": category_element.category_name,
        "კატეგორიის აღწერა": category_element.category_description
    }
    parent = category_element.parent_category
    if parent:
        categories_dictionary["ზეკატეგორიის ID"] = parent.id
        categories_dictionary["ზეკატეგორია"] = parent.category_name

    return JsonResponse(
        categories_dictionary,
        json_dumps_params={'ensure_ascii': False}
    )


def product(request, product_id):
    product_element = Product.objects.get(id=product_id)
    product_dictionary = {
        "პროდუქტის სახელი": product_element.product_name,
        "პროდუქტის აღწერა": product_element.product_description,
        "პროდუქტის ფასი": product_element.product_price
    }
    categories = product_element.product_category.all()
    category_list = []
    for cat in categories:
        category_list.append(cat.category_name)

    product_dictionary["პროდუქტის კატეგორიები"] = category_list
    return JsonResponse(
        product_dictionary,
        json_dumps_params={'ensure_ascii': False}
    )
