from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views import generic
from django.views import View

from shop.forms import (BoardGameForm,
                        BoardgameSearchForm,
                        AuthorCreationForm,
                        AuthorUpdateForm,
                        AuthorSearchForm,
                        PublisherSearchForm)
from shop.models import (Publisher,
                         Author,
                         BoardGame)


# Create your views here.
@login_required()
def index(request):
    """View function for the home page of the site."""
    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1
    context = {
        "num_visits": num_visits + 1,
    }

    return render(request, "shop/index.html", context=context)


class PublisherListView(LoginRequiredMixin, generic.ListView):
    model = Publisher
    context_object_name = "publisher_list"
    template_name = "shop/publisher_list.html"
    paginate_by = 5
    queryset = Publisher.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PublisherListView, self).get_context_data(**kwargs)
        name = self.request.GET.get("name", "")
        context["search_form"] = PublisherSearchForm(initial={"name": name})
        return context

    def get_queryset(self):
        form = PublisherSearchForm(self.request.GET)
        if form.is_valid():
            return self.queryset.filter(
                name__icontains=form.cleaned_data["name"])
        return self.queryset


class PublisherCreateView(LoginRequiredMixin, generic.CreateView):
    model = Publisher
    fields = "__all__"
    success_url = reverse_lazy("shop:publisher-list")


class PublisherUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Publisher
    fields = "__all__"
    success_url = reverse_lazy("shop:publisher-list")


class PublisherDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Publisher
    success_url = reverse_lazy("shop:publisher-list")


class AuthorListView(LoginRequiredMixin, generic.ListView):
    model = Author
    context_object_name = "author_list"
    template_name = "shop/author_list.html"
    paginate_by = 10
    queryset = Author.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(AuthorListView, self).get_context_data(**kwargs)
        username = self.request.GET.get("username", "")
        context["search_form"] = AuthorSearchForm(initial={"username": username})
        return context

    def get_queryset(self):
        form = AuthorSearchForm(self.request.GET)
        if form.is_valid():
            return self.queryset.filter(
                username__icontains=form.cleaned_data["username"])
        return self.queryset


class AuthorDetailView(LoginRequiredMixin, generic.DetailView):
    model = Author
    context_object_name = "author_detail"
    template_name = "shop/author_detail.html"
    # queryset = Author.objects.all().prefetch_related("boardgame__publisher")


class AuthorCreateView(LoginRequiredMixin, generic.CreateView):
    model = Author
    form_class = AuthorCreationForm


class AuthorDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Author
    success_url = reverse_lazy("")


class AuthorUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Author
    form_class = AuthorUpdateForm
    success_url = reverse_lazy("shop:author-list")


class BoardgameListView(LoginRequiredMixin, generic.ListView):
    model = BoardGame
    context_object_name = "boardgame_list"
    template_name = "shop/boardgame_list.html"
    queryset = BoardGame.objects.all().select_related("publisher")

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(BoardgameListView, self).get_context_data(**kwargs)
        name = self.request.GET.get("name", "")
        context["search_form"] = BoardgameSearchForm(initial={"name": name})
        return context

    def get_queryset(self):
        form = BoardgameSearchForm(self.request.GET)
        if form.is_valid():
            return self.queryset.filter(
                name__icontains=form.cleaned_data["name"])
        return self.queryset


class BoardgameDetailView(LoginRequiredMixin, generic.DetailView):
    model = BoardGame


class BoardgameCreateView(LoginRequiredMixin, generic.CreateView):
    model = BoardGame
    form_class = BoardGameForm
    success_url = reverse_lazy("shop:boardgame-list")


class BoardgameUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = BoardGame
    form_class = BoardGameForm
    success_url = reverse_lazy("shop:boardgame-list")


class BoardgameDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = BoardGame
    success_url = reverse_lazy("shop:boardgame-list")


class Assign(View):
    @login_required
    def post(request, pk):
        author = Author.objects.get(id=request.user.id)
        if BoardGame.objects.get(id=pk) in author.boardgames.all():
            author.boardgames.remove(pk)
        else:
            author.boardgames.add(pk)
        return HttpResponseRedirect(reverse_lazy("shop:boardgame-detail", args=[pk]))


class Logout(View):
    @staticmethod
    def post(request):
        logout(request)
        return HttpResponseRedirect(reverse('shop:index'))
