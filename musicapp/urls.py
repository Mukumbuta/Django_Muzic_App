from django.urls import path
from musicapp import views

urlpatterns = [
    path('artists/', views.artiste_list),
    path('songs/', views.song_list),
    path('artists/<int:pk>/', views.artiste_details),
    path('songs/<int:pk>/', views.song_details),
]