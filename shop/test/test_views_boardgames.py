from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from shop.models import BoardGame, Publisher

BOARD_GAME_URL = reverse("shop:boardgame-list")


class PublicBoardgameTest(TestCase):
    def test_login_required(self) -> None:
        res = self.client.get(BOARD_GAME_URL)
        self.assertNotEqual(res.status_code, 200)


class PrivateBoardgameTest(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="test",
            password="12345",
        )
        self.client.force_login(self.user)

    def test_retrieve_boardgame(self) -> None:
        publisher = Publisher.objects.create(name="Bomba")
        BoardGame.objects.create(name="first", publisher=publisher)
        BoardGame.objects.create(name="second", publisher=publisher)
        response = self.client.get(BOARD_GAME_URL)
        self.assertEqual(response.status_code, 200)

        boardgame = BoardGame.objects.all()
        self.assertEqual(list(response.context["boardgame_list"]), list(boardgame))

        self.assertTemplateUsed(response, "shop/boardgame_list.html")
