from django.urls import path
from .views import RouterView, IndexView, RouterDetailsView, edit, create,delete
from django.contrib import admin

app_name = "app1"

# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('routers/', RouterView.as_view()),
    path('router/<int:pk>', RouterView.as_view()),
    path('details/', IndexView.as_view(), name='index'),
    path('details/<int:pk>/', RouterDetailsView.as_view(), name='detail'),
    path('details/edit/<int:pk>/', edit, name='edit'),
    path('details/create/', create, name='create'),
    path('details/delete/<int:pk>/', delete, name='delete'),
]
