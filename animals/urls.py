from django.urls import path

from . import views as Animal_views

urlpatterns = [
    path("animals/", Animal_views.AnimalView.as_view()),
    path("animals/<int:animal_id>/", Animal_views.AnimalDetailView.as_view()),
]