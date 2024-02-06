from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.test import TestCase
from django.urls import reverse

from shop.forms import AuthorCreationForm
from shop.models import Author

AUTHOR_URL = reverse("shop:author-list")


class PublicAuthorTest(TestCase):
    def test_login_required(self) -> None:
        res = self.client.get(AUTHOR_URL)
        self.assertNotEqual(res.status_code, 200)


class PrivateAuthorTest(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="test",
            password="12345ps.",
        )
        self.client.force_login(self.user)
