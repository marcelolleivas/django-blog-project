from django.test import TestCase

from .conftest import PostFactory


class TestModelPost(TestCase):
    def setUp(self) -> None:
        self.post = PostFactory()

    def test_str_method_returns_title(self) -> None:
        # Given
        expected = "Lorem ipsum dolor"
        result = str(self.post.__str__())
        # Then
        self.assertEqual(expected, result)
