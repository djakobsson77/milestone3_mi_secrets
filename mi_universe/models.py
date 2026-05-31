from django.db import models


GAME_CHOICES = [
    ("Unknown", "Unknown"),
    ("The Secret of Monkey Island", "The Secret of Monkey Island"),
    (
        "Monkey Island 2 – LeChuck's Revenge",
        "Monkey Island 2 – LeChuck's Revenge"
    ),
    ("The Curse of Monkey Island", "The Curse of Monkey Island"),
    ("Escape from Monkey Island", "Escape from Monkey Island"),
    ("Tales of Monkey Island", "Tales of Monkey Island"),
    ("Return to Monkey Island", "Return to Monkey Island"),
]


class Island(models.Model):
    name = models.CharField(max_length=100)
    game = models.CharField(max_length=100, choices=GAME_CHOICES)
    description = models.TextField()
    image_file = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name


class Character(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image_file = models.CharField(max_length=200, blank=True)
    island = models.ForeignKey(Island, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class PirateItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image_file = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name
