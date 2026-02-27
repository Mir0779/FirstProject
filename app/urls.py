from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('', views.index, name='index'),
    path('notes/', views.liste_notes, name='listeNotes'),
    path('notes/new/', views.create_note, name='CreateNote'),
    path('notes/edit/<int:pk>/', views.update_note, name='EditNote'),
    path('notes/delete/<int:pk>/', views.delete_note, name='DeleteNote'),
]
