from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile_detail, name='profile'),
    path('likes/', views.profile_like, name='like')
]
