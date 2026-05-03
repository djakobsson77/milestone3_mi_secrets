from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Game(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.CharField(max_length=200)

    def __str__(self):
        return self.title
    

class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey('Game', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.game.title} x {self.quantity}"

    @property
    def total_price(self):
        return self.game.price * self.quantity
