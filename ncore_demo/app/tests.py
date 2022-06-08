from django.test import TestCase
from core.models import Item


class PostTestCase(TestCase):
    def testPost(self):
        item = Item(title="My Title", description="Blurb",
                    category="shirt", slug="test", price=100)
        self.assertEqual(item.title, "My Title")
        self.assertEqual(item.description, "Blurb")
        self.assertEqual(item.category, "shirt")
        self.assertEqual(item.slug, "test")
        self.assertEqual(item.price, 100)
