from django.test import TestCase
from ..serializers import UserSerializer


class UserSerializerTestCase(TestCase):
    def setUp(self):
        self.user_data = {
            'nickname': 'testuser',
            'name': 'Test User',
            'email': 'test@example.com',
            'age': 25
        }

    # Teste de validação do Serializer
    def test_user_serializer(self):
        serializer = UserSerializer(data=self.user_data)
        self.assertTrue(serializer.is_valid())

        # Verifica se os dados serializados estão corretos
        serialized_data = serializer.data
        self.assertEqual(
            serialized_data['nickname'],
            self.user_data['nickname']
        )
        self.assertEqual(serialized_data['name'], self.user_data['name'])
        self.assertEqual(
            serialized_data['email'],
            self.user_data['email']
        )
        self.assertEqual(int(
            serialized_data['age']),
            int(self.user_data['age'])
        )
        # Convertendo para int para lidar com possíveis diferenças de tipo
