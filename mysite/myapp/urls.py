from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),
    path('search_by_name/', views.search_by_name, name='search_by_name'),
    path('edit_course/<code>/', views.edit_course, name='edit_course'),
    path('delete_course/', views.delete_course, name='delete_course_no_code'),  # New pattern without code
    path('delete_course/<code>/', views.delete_course, name='delete_course'),  # Original pattern with code
]
