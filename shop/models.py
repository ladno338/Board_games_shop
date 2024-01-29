from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class Publisher(models.Model):
    name = models.CharField(max_length=255, unique=True)
    country = models.CharField(max_length=255)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"{self.name} {self.country}"


class Author(AbstractUser):
    country = models.CharField(max_length=255)

    class Meta:
        verbose_name = "author"
        verbose_name_plural = "authors"

    def __str__(self):
        return f"{self.username} ({self.first_name} {self.last_name})"


class BoardGame(models.Model):
    name = models.CharField(max_length=255)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, related_name="boardgame")
    authors = models.ManyToManyField(Author, related_name="boardgames")

    class Meta:
        ordering = ("name", )

    def __str__(self):
        return self.name
