from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView

from .forms import CommentCreationForm
from .models import Client, OwnedCar


class ClientListView(LoginRequiredMixin, ListView):
    model = Client
    template_name = 'client_list.html'

    # Filter the clients list to only display the clients created by the logged in employee
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

    # Assign the logged in employee's username as the author and validate the form by calling the form_valid() of the
    # super class.
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


# This is a form based view and this function is executed only if application is logged in.
@login_required
def comment_new(request):
    if request.method == "POST":
        form = CommentCreationForm(request.POST)
        # Assign the username of the logged in employee to the author field of the comment.
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

    # Assign the logged in employee's username as the author and validate the form by calling the form_valid() of the
    # super class.
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class OwnedCarDeleteView(LoginRequiredMixin, DeleteView):
    model = OwnedCar
    template_name = 'ownedcar_delete.html'
    success_url = reverse_lazy('client_list')


class OwnedCarUpdateView(LoginRequiredMixin, UpdateView):
    model = OwnedCar
    fields = ('client', 'manufacturer', 'car_model', 'date_of_purchase', 'date_of_last_service')
    template_name = 'ownedcar_edit.html'
    success_url = reverse_lazy('client_list')
