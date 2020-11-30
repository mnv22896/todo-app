from django.urls import path

from . import views
app_name='todo'
urlpatterns = [
     path('todo/', views.todo_view),
    path('addTodo/', views.add_todo),
    path('deleteTodo/<int:todo_id>/', views.delete_todo),
]
   
