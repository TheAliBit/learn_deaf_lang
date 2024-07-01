from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile_detail),
    #path('words/', views.word_list),
    #path('words/<int:pk>', views.word_detail)
]
