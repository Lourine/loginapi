from django.urls import path

from . import views

urlpatterns = [
    path('users/', views.MyUserList.as_view()),
    path('users/<int:pk>/', views.MyUserDetail.as_view()),
]