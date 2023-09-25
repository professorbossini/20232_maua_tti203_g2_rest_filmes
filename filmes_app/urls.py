from django.urls import path
from . import views

urlpatterns = [
  path(
    'filmes/',
    views.FilmeListCreate.as_view(),
    name='filme-list-create'
  )
]