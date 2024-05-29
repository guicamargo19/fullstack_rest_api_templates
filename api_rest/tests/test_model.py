from django.test import TestCase
from ..models import User
from django.core.exceptions import ValidationError


class ProductModelTestCase(TestCase):
    def setUp(self):
        self.valid_user_data = {
            'nickname': 'testuser',
            'name': 'Test User',
            'email': 'test@example.com',
            'age': 25
        }

    # Criação de um usuário
    def test_valid_product_creation(self):
        user = User.objects.create(**self.valid_user_data)
        self.assertEqual(user.nickname, self.valid_user_data['nickname'])
        self.assertEqual(user.name, self.valid_user_data['name'])
        self.assertEqual(user.email,
                         self.valid_user_data['email'])
        self.assertEqual(user.age, int(
            self.valid_user_data['age']))

    # Dado inválido para o campo age
    def test_invalid_user_creation_invalid_value(self):
        invalid_user_data = {
            'nickname': 'testuser',
            'name': 'Test User',
            'email': 'test@example.com',
            'age': 'dado inválido'
        }
        with self.assertRaises(ValueError):
            User.objects.create(**invalid_user_data)

    # Campo name faltando preencher
    def test_invalid_user_creation_missing_fields(self):
        invalid_user_data = {
            'nickname': 'testuser',
            # 'name': 'Test User',
            'email': 'test@example.com',
            'age': 25
        }

        invalid_user = User(**invalid_user_data)

        with self.assertRaises(ValidationError):
            invalid_user.full_clean()

    # Valor negativo no campo age
    def test_invalid_product_creation_negative_value(self):
        invalid_user_data = {
            'nickname': 'testuser',
            'name': 'Test User',
            'email': 'test@example.com',
            'age': -25
        }

        invalid_user = User(**invalid_user_data)

        with self.assertRaises(ValidationError):
            invalid_user.full_clean()
