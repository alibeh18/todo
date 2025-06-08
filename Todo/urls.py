from django.urls import path
from Todo.views import *

urlpatterns = [
    path('todos/', todo_list),
    path('todos/create/', create_todo),
    path('todos/<int:pk>/', todo_detail),
    path('todos/<int:pk>/update/', update_todo),
    path('todos/<int:pk>/delete/', delete_todo),
]