import factory
import pytest
from django.contrib.auth.models import User

from ..models import Post


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    email = "teste@teste.com"
    username = "teste"
    password = factory.PostGenerationMethodCall("set_password", "@adm1n")


class PostFactory(factory.Factory):
    class Meta:
        model = Post

    title = "Lorem ipsum dolor"
    slug = "lorem-ipsum-dolor"
    content = factory.Faker("sentence", nb_words=60)
    author = factory.SubFactory(UserFactory)
