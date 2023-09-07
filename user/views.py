from django.shortcuts import render
from .models import CustomUser
from .forms import CreateNewUserForm
from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView, CreateView, ModelFormMixin
from django.urls import reverse_lazy



class UserListView(ListView):
	model = CustomUser
	paginate_by = 20
	template_name = 'list_user.html'
	context_object_name = 'user_list'

	def get_queryset(self, *args, **kwargs):
		queryset = super(UserListView, self).get_queryset(*args, **kwargs)
		queryset = queryset.values('uuid', 'first_name', 'last_name', 'email', 'is_active')
		return queryset



class DeleteUserView(DeleteView):
	model = CustomUser
	template_name = 'delete_user.html'
	success_url = reverse_lazy('user:list_user')



class CreateNewUserView(CreateView, ModelFormMixin):
	template_name = 'signup_user.html'
	form_class = CreateNewUserForm
	success_url = reverse_lazy('user:list_user')

	def form_valid(self, form):
		return super().form_valid(form)