from .models import User
from .serializers import UserSerializer
from rest_framework import viewsets
from .forms import UserForm
from django.views import View
from django.shortcuts import render, redirect
from django.db.models import Q
from django.core.paginator import Paginator


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    ordering = '-id'


# Views para renderizar os templates HTML
class UserListView(View):
    def get(self, request):
        users = User.objects.all().order_by('-id')

        paginator = Paginator(users, 4)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)

        return render(request, 'users/user_list.html', {'users': page_obj})


class UserSearchListView(View):
    def get(self, request):
        search_value = self.request.GET.get('q', '').strip()

        if search_value == '':
            return redirect('user_list')

        users = User.objects.filter(
            Q(nickname__icontains=search_value) |
            Q(name__icontains=search_value) |
            Q(email__icontains=search_value) |
            Q(age__icontains=search_value)
        )

        paginator = Paginator(users, 4)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)

        return render(request, 'users/user_list.html', {'users': page_obj})


class UserDeleteAll(View):
    def get(self, request):
        users = User.objects.all()
        if len(users) != 0:
            return render(request, 'users/delete_all.html', {
                'users': users,
            })
        return render(request, 'users/user_list.html', {'users': users})

    def post(self, request):
        users = User.objects.all()
        users.delete()
        return redirect('user_list')


class UserCreateView(View):
    def get(self, request):
        form = UserForm()
        return render(
            request,
            'users/user_form.html',
            {
                'form': form,
                'title': 'Criar usuário',
                'button_text': 'Criar',
            }
        )

    def post(self, request):
        form = UserForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('user_list')
        return render(
            request,
            'users/user_form.html',
            {
                'form': form,
                'title': 'Criar usuário',
                'button_text': 'Criar',
            }
        )


class UserUpdateView(View):
    def get(self, request, id):
        user = User.objects.get(pk=id)
        form = UserForm(instance=user)
        return render(
            request,
            'users/user_form.html',
            {
                'form': form,
                'title': 'Atualizar usuário',
                'button_text': 'Atualizar',
            }
        )

    def post(self, request, id):
        user = User.objects.get(pk=id)
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_list')
        return render(
            request,
            'users/user_form.html',
            {
                'form': form,
                'title': 'Atualizar usuário',
                'button_text': 'Atualizar',
            }
        )


class UserDeleteView(View):
    def get(self, request, id):
        user = User.objects.get(pk=id)
        return render(request, 'users/user_delete.html', {'user': user})

    def post(self, request, id):
        user = User.objects.get(pk=id)
        user.delete()
        return redirect('user_list')
