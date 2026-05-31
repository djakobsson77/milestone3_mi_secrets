from urllib import request
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Game, CartItem

# Create your views here.


@login_required
def shop(request):
    games = Game.objects.all()
    cart_count = 0

    if request.user.is_authenticated:
        cart_count = CartItem.objects.filter(user=request.user).count()

    return render(request, 'shop/shop.html', {
        'games': games,
        'cart_count': cart_count
    })


@login_required
def add_to_cart(request, game_id):
    game = get_object_or_404(Game, id=game_id)
    cart_item, created = CartItem.objects.get_or_create(
        user=request.user,
        game=game,
        defaults={'quantity': 1}
    )

    if not created:
        cart_item.quantity += 1
        cart_item.save()
        messages.success(
            request,
            f'{game.title} quantity updated in your cart.'
        )
    else:
        messages.success(
            request,
            f'{game.title} added to your cart.'
        )
    return redirect(request.META.get('HTTP_REFERER', 'shop'))


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
            messages.success(
                request,
                f'{item.game.title} quantity updated.'
            )
        else:
            item.delete()
            messages.success(
                request,
                f'{item.game.title} removed from your cart.'
            )

    return redirect('cart')


@login_required
def remove_from_cart(request, item_id):
    item = get_object_or_404(CartItem, id=item_id, user=request.user)
    game_title = item.game.title
    item.delete()
    messages.success(
        request,
        f'{game_title} removed from your cart.'
    )
    return redirect('cart')


@login_required
def checkout(request):
    CartItem.objects.filter(user=request.user).delete()
    return render(request, 'shop/checkout.html')
