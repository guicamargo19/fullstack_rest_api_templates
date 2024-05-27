from django.db import models


class User(models.Model):
    nickname = models.CharField(
        max_length=100, default='', null=False, blank=False)
    name = models.CharField(
        max_length=150, default='', null=False, blank=False)
    email = models.EmailField(default='', null=False, blank=False)
    age = models.PositiveIntegerField(default=0, null=False, blank=False)

    def __str__(self):
        return (
            f'Nome: {self.name} | E-mail: {self.email}'
        )
