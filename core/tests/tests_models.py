from django.test import TestCase
from django.urls import reverse

from .conftest import PostFactory


class TestModelPost(TestCase):
    def setUp(self) -> None:
        self.post = PostFactory()

    def test_absolute_url_delete(self) -> None:
        # Given
        url = self.post.get_absolute_url_delete()
        # Then
        self.assertEqual(url, "/post/lorem-ipsum-dolor/delete/")

    def test_absolute_url_update(self) -> None:
        # Given
        url = self.post.get_absolute_url_update()
        # Then
        self.assertEqual(url, "/post/lorem-ipsum-dolor/edit/")

    def test_absolute_url(self) -> None:
        # Given
        url = self.post.get_absolute_url()
        # Then
        self.assertEqual(url, "/post/lorem-ipsum-dolor/")

    def test_str_method_returns_title(self) -> None:
        # Given
        expected = "Lorem ipsum dolor"
        result = str(self.post.__str__())
        # Then
        self.assertEqual(expected, result)
