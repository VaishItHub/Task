from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('clients/', views.client_list, name='client_list'),
    path('clients/register/', views.register_client, name='register_client'),
    path('clients/<int:client_id>/edit/', views.edit_client, name='edit_client'),
    path('clients/<int:client_id>/delete/', views.delete_client, name='delete_client'),
    path('clients/<int:client_id>/projects/add/', views.add_project, name='add_project'),
    path('projects/', views.user_projects, name='user_projects'),
    path('clients/<int:client_id>/', views.client_detail, name='client_detail'),  # Fix this line
    path('accounts/logout/', LogoutView.as_view(next_page='/'), name='logout'),  # Redirect to homepage after logout
]