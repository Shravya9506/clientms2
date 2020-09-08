from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.views.generic import ListView, DetailView
from .models import models
from .models import Client, Comment, OwnedCar
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CommentCreationForm

class ClientListView(LoginRequiredMixin, ListView):
    model = Client
    template_name = 'client_list.html'

    def get_queryset(self):
        user_id = self.request.user
        return Client.objects.filter(author=user_id)


class ClientDetailView(LoginRequiredMixin, DetailView):
    model = Client
    template_name = 'client_detail.html'
    login_url = 'login'


class ClientUpdateView(LoginRequiredMixin, UpdateView):
    model = Client
    fields = ('name', 'notes', 'address', 'city', 'state', 'zipcode', 'email', 'cell_phone', 'acct_number')
    template_name = 'client_edit.html'


class ClientDeleteView(LoginRequiredMixin, DeleteView):
    model = Client
    template_name = 'client_delete.html'
    success_url = reverse_lazy('client_list')

class ClientCreateView(LoginRequiredMixin, CreateView):
    model = Client
    template_name = 'client_new.html'
    fields = ('name', 'notes', 'address', 'city', 'state', 'zipcode', 'email', 'cell_phone', 'acct_number')
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


@login_required
def comment_new(request):
    if request.method == "POST":
        form = CommentCreationForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.save()
            return redirect('client_list')
    else:
        form = CommentCreationForm()
    return render(request, 'comment_new.html', {'form': form})

class OwnedCarCreateView(LoginRequiredMixin, CreateView):
    model = OwnedCar
    template_name = 'ownedcar_new.html'
    fields = ('client', 'manufacturer', 'car_model', 'date_of_purchase', 'date_of_last_service')
    success_url = reverse_lazy('client_list')

    def form_valid(self, form):
        self.instance.author = self.request.user
        return super().form_valid(form)


class OwnedCarDeleteView(LoginRequiredMixin, DeleteView):
    model = OwnedCar
    template_name = 'ownedcar_delete.html'
    success_url = reverse_lazy('client_list')


class OwnedCarUpdateView(LoginRequiredMixin, UpdateView):
    model = OwnedCar
    fields = ('client', 'manufacturer', 'car_model', 'date_of_purchase', 'date_of_last_service')
    template_name = 'ownedcar_edit.html'

