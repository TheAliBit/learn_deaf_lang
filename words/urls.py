from django.urls import path
from . import views

urlpatterns = [
    path('category/', views.category_view, name='category_view'),
    path('category/<int:pk>/', views.category_view, name='category_view'),
    path('detail/<str:slug>/', views.word_detail_view, name='word_detail_view'),
    path('like/<str:slug>/', views.like_word, name='like_word'),
    path('unlike/<str:slug>/', views.unlike_word, name='unlike_word'),
]