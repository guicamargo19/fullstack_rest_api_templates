from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from ..models import User
from ..serializers import UserSerializer


class UserAPITest(APITestCase):

    def setUp(self):
        self.user = User.objects.create(
            nickname='testuser',
            name='Test User',
            email='test@example.com',
            age=25
        )
        self.url = reverse('user-list')

    def test_get_users(self):
        response = self.client.get(self.url)
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_create_user(self):
        data = {
            'nickname': 'newuser',
            'name': 'New User',
            'email': 'new@example.com',
            'age': 30
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 2)
        self.assertEqual(User.objects.get(id=2).nickname, 'newuser')

    def test_update_user(self):
        url = reverse('user-detail', args=[self.user.id])  # type: ignore
        data = {
            'nickname': 'updateduser',
            'name': 'Updated User',
            'email': 'updated@example.com',
            'age': 35
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.user.refresh_from_db()
        self.assertEqual(self.user.nickname, 'updateduser')

    def test_delete_user(self):
        url = reverse('user-detail', args=[self.user.id])  # type: ignore
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(User.objects.count(), 0)
