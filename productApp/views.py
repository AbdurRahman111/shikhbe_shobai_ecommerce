from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from .models import product_table, Cart, CartItem
from django.http import JsonResponse
# Create your views here.


@login_required
def add_to_cart_ajax(request):
    if request.method == "POST":
        product_id = request.POST.get("product_id")
        quantity = request.POST.get("quantity")
        print(product_id)
        print(quantity)
        # product = product_table.objects.get(id=product_id)
        product = get_object_or_404(product_table, id=product_id)
        print(product)

        user = request.user
        cart, _ = Cart.objects.get_or_create(user=user)
        cart_item, created = CartItem.objects.get_or_create(
            cart=cart,
            product=product,
            quantity=int(quantity)
        )
        if not created:
            cart_item.quantity += int(quantity)
        cart_item.save()

        total_items = cart.items.count()

        return JsonResponse({
            "status": "success",
            "message": "Product Added to Cart!",
            'cart_items': total_items,
            "quantity": cart_item.quantity
        })
    return JsonResponse({"status": "error"}, status=400)