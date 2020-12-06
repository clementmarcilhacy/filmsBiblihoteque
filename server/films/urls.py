from django.urls import path
from .views import (
    home_view,
    films_list_view,
    film_create_view,
    film_details_view,
    film_update_view,
    film_delete_view,
     # about_view,
)

app_name = 'films'
urlpatterns = [
    path('home/', home_view, name='home'),
    #path('about/', about_view, name='about'),
    path('create/', film_create_view, name='film-create'),
    path('list/', films_list_view, name='film-list'),
    path('<int:my_id>/', film_details_view, name='film-details'),
    path('<int:my_id>/update/', film_update_view, name='film-update'),
    path('<int:my_id>/delete/', film_delete_view, name='film-delete'),
]
