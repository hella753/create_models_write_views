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
            parent_id = parent.id
            parent_name = parent.category_name
            parent_dict = {"ID": parent_id, "სახელი": parent_name}
        else:
            parent_dict = None

        categories_dictionary["ზეკატეგორია"] = parent_dict

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
        if product_element.product_image:
            image = f"{request.get_host()}{product_element.product_image.url}"
        else:
            image = None
        products_dictionary["პროდუქტის სურათი"] = image

        max_cat = (
            product_element
            .product_category
            .all()
            .aggregate(Max("category_level"))
        )
        cat = (
            product_element
            .product_category
            .all()
            .filter(category_level=max_cat['category_level__max'])
        )
        cat_list = []
        for cat_each in cat:
            cat_dict = {"ID": cat_each.id, "სახელი": cat_each.category_name}
            cat_list.append(cat_dict)
        products_dictionary["პროდუქტის კატეგორია"] = cat_list

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
        parent_id = parent.id
        parent_name = parent.category_name
        parent_dict = {"ID": parent_id, "სახელი": parent_name}
    else:
        parent_dict = None

    categories_dictionary["ზეკატეგორია"] = parent_dict
    return JsonResponse(
        categories_dictionary,
        json_dumps_params={'ensure_ascii': False}
    )


def product(request, product_id):
    product_element = Product.objects.get(id=product_id)
    product_dictionary = {
        "პროდუქტის სახელი": product_element.product_name,
        "პროდუქტის აღწერა": product_element.product_description,
        "პროდუქტის ფასი": product_element.product_price,
    }
    if product_element.product_image:
        image = f"{request.get_host()}{product_element.product_image.url}"
    else:
        image = None
    product_dictionary["პროდუქტის სურათი"] = image

    categories = product_element.product_category.all()
    category_list = []
    for cat in categories:
        cat_dict = {"ID": cat.id, "სახელი": cat.category_name}
        category_list.append(cat_dict)

    product_dictionary["პროდუქტის კატეგორიები"] = category_list
    return JsonResponse(
        product_dictionary,
        json_dumps_params={'ensure_ascii': False}
    )
