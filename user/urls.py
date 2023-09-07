from django.urls import path
from .views import UserListView, DeleteUserView, CreateNewUserView


app_name = 'user'


urlpatterns = [
	path('list_user/', UserListView.as_view(), name='list_user'),
	path('<slug:pk>/delete/', DeleteUserView.as_view(), name='delete_user'),
	path('create_user', CreateNewUserView.as_view(), name='create_user'),
]