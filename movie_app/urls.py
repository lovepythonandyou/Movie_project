from . import views
from django.urls import path, include


urlpatterns = [
    path('', views.show_all_movie),
    path('movie/<slug:slug_movie>', views.show_one_movie, name='movie-detail'),
    path('directors/', views.show_directors),
    # path('directors/<int:id>', views.show_one_director, name='movie-detail')
    path('directors/test/', views.show_one_director)
]