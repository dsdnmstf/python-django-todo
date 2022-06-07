from django.urls import path
from .views import create_todo, delete_todo, detail_todo, home, list_todo, update_todo
urlpatterns = [
    path('', home, name='home'),
    path("list/", list_todo, name ="list-todo" ),
    path('create/', create_todo, name='create-todo'),
    path('update/<int:id>', update_todo, name='update-todo'),
    path('detail/<int:id>', detail_todo, name='detail-todo'),
    path('delete/<int:id>', delete_todo, name='delete-todo'),
]
