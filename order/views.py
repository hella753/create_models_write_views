from django.http import HttpResponse, JsonResponse
from .models import Order

def index(request):
    orders = Order.objects.all()
    order_list = []
    for order in orders:
        order_dict = {
            "შეკვეთის ID": order.id,
            "შეკვეთის თარიღი": order.order_date,
            "შეკვეთის სტატუსი": order.order_status,
            "პროდუქტის ID": order.product_id.id
        }
        order_list.append(order_dict)
        order_dict={}
        print(order_list)
    return JsonResponse(order_list, safe=False)


def individual_order(request, order_id):
    order = Order.objects.get(id=order_id)
    order_dict = {
        "შეკვეთის ID": order.id,
        "შეკვეთის თარიღი": order.order_date,
        "შეკვეთის სტატუსი": order.order_status,
        "პროდუქტის ID": order.product_id.id,
        "პროდუქტის რაოდენობა": order.product_quantity,
        "შეკვეთის ჯამური ფასი": order.order_total,
        "შემკვეთი მომხმარებლის ID": order.order_customer.id,
        "შეკვეთის მისამართი": order.order_address,

    }
    return JsonResponse(order_dict, safe=False)
