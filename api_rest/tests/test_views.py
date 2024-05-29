from django.test import TestCase
from django.urls import reverse
from ..models import User


class UserViewTests(TestCase):

    def setUp(self):
        self.user = User.objects.create(
            nickname='testuser',
            name='Test User',
            email='test@example.com',
            age=25
        )

    def test_user_list_view(self):
        response = self.client.get(reverse('user_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/user_list.html')

    def test_user_create_view_get(self):
        response = self.client.get(reverse('user_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/user_form.html')

    def test_user_create_view_post(self):
        data = {
            'nickname': 'newuser',
            'name': 'New User',
            'email': 'new@example.com',
            'age': 30
        }
        response = self.client.post(reverse('user_create'), data)
        self.assertEqual(response.status_code, 302)  # Redirecionamento
        self.assertEqual(User.objects.count(), 2)

    def test_user_update_view_get(self):
        response = self.client.get(
            reverse('user_update', args=[self.user.id])  # type: ignore
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/user_form.html')

    def test_user_update_view_post(self):
        data = {
            'nickname': 'updateduser',
            'name': 'Updated User',
            'email': 'updated@example.com',
            'age': 35
        }
        response = self.client.post(
            reverse('user_update', args=[self.user.id]), data  # type: ignore
        )
        self.assertEqual(response.status_code, 302)  # Redirecionamento
        self.user.refresh_from_db()
        self.assertEqual(self.user.nickname, 'updateduser')

    def test_user_delete_view_get(self):
        response = self.client.get(
            reverse('user_delete', args=[self.user.id])  # type: ignore
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/user_delete.html')

    def test_user_delete_view_post(self):
        response = self.client.post(
            reverse('user_delete', args=[self.user.id])  # type: ignore
        )
        self.assertEqual(response.status_code, 302)  # Redirecionamento
        self.assertEqual(User.objects.count(), 0)
