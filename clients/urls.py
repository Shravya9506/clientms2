
from django.urls import path
from .views import (
    ClientListView,
    ClientUpdateView,
    ClientDetailView,
    ClientDeleteView,
    ClientCreateView,
    OwnedCarCreateView,
    OwnedCarUpdateView,
    OwnedCarDeleteView
)
from . import views

urlpatterns = [
    path('<int:pk>/edit/', ClientUpdateView.as_view(), name='client_edit'),
    path('<int:pk>/', ClientDetailView.as_view(), name='client_detail'),
    path('<int:pk>/delete/', ClientDeleteView.as_view(), name='client_delete'),
    path('', ClientListView.as_view(), name='client_list'),
    path('new/', ClientCreateView.as_view(), name='client_new'),
    path('comment/new/', views.comment_new, name='comment_new'),
    path('ownedcar/new/', OwnedCarCreateView.as_view(), name='ownedcar_new'),
    path('ownedcar/<int:pk>/edit/', OwnedCarUpdateView.as_view(), name='ownedcar_edit'),
    path('ownedcar/<int:pk>/delete/', OwnedCarDeleteView.as_view(), name='ownedcar_delete'),
]
