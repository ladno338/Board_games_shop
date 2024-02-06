from django.contrib.auth import get_user_model
from django.test import TestCase

from shop.models import Publisher, BoardGame


# Create your tests here.
class Modelstests(TestCase):
    def test_publisher_str(self) -> None:
        publisher = Publisher.objects.create(name="test")
        self.assertEqual(
            str(publisher), f"{publisher.name} {publisher.country}"
        )

    def test_author_str(self) -> None:
        author = get_user_model().objects.create(
            username="test",
            password="12345",
            first_name="test_first",
            last_name="test_last",
        )
        self.assertEqual(
            str(author),
            f"{author.username}"
            f" ({author.first_name}"
            f" {author.last_name})",
        )

    def test_boardgame_str(self) -> None:
        publisher = Publisher.objects.create(name="test")
        boardgame = BoardGame.objects.create(name="X", publisher=publisher)
        self.assertEqual(str(boardgame), boardgame.name)

    def test_author_license_number(self) -> None:
        username = "test"
        password = "12345"
        author = get_user_model().objects.create_user(
            username=username,
            password=password,
            first_name="test_first",
            last_name="test_last",
        )
        self.assertEqual(author.username, username)
        self.assertTrue(author.check_password(password))
