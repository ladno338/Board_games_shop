from django.urls import path

from shop.views import (index,
                        PublisherListView,
                        AuthorListView,
                        AuthorDetailView,
                        BoardgameListView,
                        BoardgameDetailView,
                        PublisherCreateView,
                        PublisherUpdateView,
                        PublisherDeleteView,
                        BoardgameCreateView,
                        BoardgameUpdateView,
                        BoardgameDeleteView,
                        AuthorCreateView,
                        AuthorUpdateView,
                        AuthorDeleteView,
                        toggle_assign_to_boardgame,
                        logout_view)

urlpatterns = [
    path("", index, name="index"),
    path("publishers/", PublisherListView.as_view(), name="publisher-list"),
    path("publishers/create/", PublisherCreateView.as_view(), name="publisher-create"),
    path("publishers/<int:pk>/update/", PublisherUpdateView.as_view(), name="publisher-update"),
    path("publishers/<int:pk>/delete/", PublisherDeleteView.as_view(), name="publisher-delete"),
    path("authors/", AuthorListView.as_view(), name="author-list"),
    path("authors/<int:pk>/", AuthorDetailView.as_view(), name="author-detail"),
    path("authors/create/", AuthorCreateView.as_view(), name="author-create"),
    path("authors/<int:pk>/update/", AuthorUpdateView.as_view(), name="author-update"),
    path("authors/<int:pk>/delete/", AuthorDeleteView.as_view(), name="author-delete"),
    path("boardgame/", BoardgameListView.as_view(), name="boardgame-list"),
    path("boardgame/create/", BoardgameCreateView.as_view(), name="boardgame-create"),
    path("boardgame/<int:pk>/update/", BoardgameUpdateView.as_view(), name="boardgame-update"),
    path("boardgame/<int:pk>/delete/", BoardgameDeleteView.as_view(), name="boardgame-delete"),
    path("boardgame/<int:pk>/", BoardgameDetailView.as_view(), name="boardgame-detail"),
    path("cars/<int:pk>/toggle-assign/", toggle_assign_to_boardgame, name="toggle-boardgame-assign"),
    path('accounts/logout/', logout_view, name='logout'),
]

app_name = "shop"
