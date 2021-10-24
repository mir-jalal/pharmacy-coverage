from unittest import TestCase
from product import Product


class ProductTest(TestCase):

    def setUp(self):
        self.product = Product(0, "testName", "testSubtitle", "testDescription", 10)

    def test_add_tag(self):
        actual = self.product.add_tag("tag")
        self.assertEqual(actual, True)
        self.assertEqual("tag", self.product.tags[-1])
        actual = self.product.add_tag("tag")
        self.assertEqual(actual, False)

    def test_get_tags(self):
        self.product.tags = ["tag1", "tag2", "tag3"]
        product_tags = self.product.get_tags()
        self.assertEqual(self.product.tags, product_tags)

    def test_remove_tags(self):
        self.product.tags = ["tag1", "tag2", "tag3"]
        actual = self.product.remove_tag("tag3")
        self.assertEqual(True, actual)
        self.assertEqual(self.product.tags, ["tag1", "tag2"])
        actual = self.product.remove_tag("tag")
        self.assertEqual(False, actual)

    def test_clear_tags(self):
        self.product.tags = ["tag1", "tag2", "tag3"]
        self.product.clear_tags()
        self.assertEqual([], self.product.tags)

    def test_increase_quantity(self):
        self.product.quantity = 0
        self.product.increase_quantity()
        self.assertEqual(1, self.product.quantity)

    def test_decrease_quantity(self):
        self.product.quantity = 10
        self.product.decrease_quantity()
        self.assertEqual(9, self.product.quantity)
