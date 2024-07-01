from django.urls import path
from . import views

urlpatterns = [
    path('category/', views.category_list, name= 'get_categories'),
    path('category/<int:pk>/children', views.category_children, name='get_children')
    #path('words/', views.word_list),
    #path('words/<int:pk>', views.word_detail)
]
