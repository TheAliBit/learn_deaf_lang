from django.urls import path
from . import views

urlpatterns = [
    # path('category/', views.category_view, name='get_categories'),
    # path('category/<int:pk>/', views.category_view, name='get_children'),
    # path('words/<int:id>', views.world_list, name='get_words')
    # path('words/<int:pk>', views.word_detail)

    path('category/', views.category_view, name='category_view'),
    path('category/<int:pk>/', views.category_view, name='category_view'),
    path('detail/<str:slug>/', views.word_detail_view, name='word_detail_view')

]
