from django.urls import path

from . import views


urlpatterns = [
    path('<int:pk>/',views.TodoDetail.as_view()),
    path('',views.TodoList.as_view()),
    path('create/',views.TodoCreate.as_view()),
    path('delete/<int:pk>/',views.TodoDelete.as_view())
]