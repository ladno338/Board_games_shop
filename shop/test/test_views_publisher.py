from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from shop.models import Publisher

PUBLISHER_URL = reverse("shop:publisher-list")


class PublicPublisherTest(TestCase):
    def test_login_required(self) -> None:
        res = self.client.get(PUBLISHER_URL)
        self.assertNotEqual(res.status_code, 200)


class PrivatePublisherTest(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="test",
            password="12345",
        )
        self.client.force_login(self.user)

    def test_retrieve_publisher(self) -> None:
        Publisher.objects.create(name="Bomba")
        Publisher.objects.create(name="DnD")
        response = self.client.get(PUBLISHER_URL)
        self.assertEqual(response.status_code, 200)

        publisher = Publisher.objects.all()
        self.assertEqual(
            list(response.context["publisher_list"]), list(publisher)
        )

        self.assertTemplateUsed(response, "shop/publisher_list.html")
