from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Game, CartItem

# Create your views here.

@login_required
def shop(request):
    games = Game.objects.all()
    return render(request, "shop/shop.html", {"games": games})


@login_required
def add_to_cart(request, game_id):
    print("USER:", request.user)
    print("GAME ID:", game_id)
    game = get_object_or_404(Game, id=game_id)
    cart_item, created = CartItem.objects.get_or_create(
        user=request.user,
        game=game,
        defaults={'quantity': 1}
    )

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('cart')


@login_required
def cart(request):
    items = CartItem.objects.filter(user=request.user)
    total = sum(item.total_price for item in items)

    return render(request, 'shop/cart.html', {
        'items': items,
        'total': total
    })


@login_required
def update_cart(request, item_id):
    item = get_object_or_404(CartItem, id=item_id, user=request.user)

    if request.method == 'POST':
        new_quantity = int(request.POST.get('quantity', 1))

        if new_quantity > 0:
            item.quantity = new_quantity
            item.save()
        else:
            item.delete()

    return redirect('cart')


@login_required
def remove_from_cart(request, item_id):
    item = get_object_or_404(CartItem, id=item_id, user=request.user)
    item.delete()
    return redirect('cart')


@login_required
def checkout(request):
    # Mock-checkout: töm kundvagnen och visa tack-sida
    CartItem.objects.filter(user=request.user).delete()
    return render(request, 'shop/checkout.html')
