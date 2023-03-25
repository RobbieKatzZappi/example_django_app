from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('clients', views.clients, name='clients'),
    path('client/<int:client_id>/', views.client, name='client'),
    path('client/<int:client_id>/request_document/', views.request_document, name='request_document')
]
