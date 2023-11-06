from django.urls import path
from .views import ToDoView, CategoryView, DeleteTodoView, ToDoDetailView, UpdateTodoView, CreateTodoView, \
    CreateCategoryView, UpdateCategoryView, DeleteCategoryView, CategoryDetailView


urlpatterns = [
    path('', ToDoView.as_view(), name='todo_list'),
    path('todo/<int:pk>/', ToDoDetailView.as_view(), name='todo_detail'),
    path('todo/<int:pk>/update', UpdateTodoView.as_view(), name='todo_upgrade'),
    path('todo/<int:pk>/delete', DeleteTodoView.as_view(), name='todo_delete'),
    path('todo/create', CreateTodoView.as_view(), name='todo_create'),

    path('categories/', CategoryView.as_view(), name='category_list'),
    path('categories/<int:pk>/delete/', DeleteCategoryView.as_view(), name='category_delete'),
    path('categories/create/', CreateCategoryView.as_view(), name='category_create'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category_detail'),
    path('categories/<int:pk>/update', UpdateCategoryView.as_view(), name='category_upgrade'),
]