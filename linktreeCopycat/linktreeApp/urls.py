from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('book/<int:book_id>', views.book_by_id, name='book_by_id'),
    #path('profile/<str:username>/', views.profile, name='profile')
    #path("user/<str:user_id>/",views.user_page, name="user_page"),
]