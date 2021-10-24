from unittest import TestCase
from cart import *


class CartTest(TestCase):

    def setUp(self):
        self.product0 = Product(0, "testName1", "testSubtitle1", "testDescription1", 10)
        self.product1 = Product(1, "testName2", "testSubtitle2", "testDescription2", 20)
        self.product2 = Product(0, "testName1", "testSubtitle1", "testDescription1", 10)
        self.product3 = Product(2, "testName1", "testSubtitle1", "testDescription1", 30)

        self.product0.quantity = 3
        self.product1.quantity = -5
        self.product2.quantity = 1
        self.product3.quantity = 1

        self.cart = Cart()

    def test_add_item(self):
        actual = self.cart.add_item(self.product1)
        self.assertEqual(actual, False)

        actual = self.cart.add_item(self.product0)
        self.assertEqual(actual, True)
        self.assertEqual(self.product0, self.cart.items[-1])

        actual = self.cart.add_item(self.product2)
        self.assertEqual(actual, True)
        self.assertEqual(4, self.cart.items[-1].quantity)

    def test_remove_item(self):
        actual = self.cart.remove_item(self.product1)
        self.assertEqual(False, actual)

        self.cart.add_item(self.product0)

        actual = self.cart.remove_item(self.product2)
        self.assertEqual(True, actual)
        self.assertEqual(2, self.cart.items[-1].quantity)

        self.cart.add_item(self.product3)

        actual = self.cart.remove_item(self.product3)
        self.assertEqual(True, actual)
        self.assertEqual(False, self.product3 in self.cart.items)

        actual = self.cart.remove_item(self.product3)
        self.assertEqual(False, actual)

    def test_get_total(self):
        self.cart.add_item(self.product0)
        self.cart.add_item(self.product2)
        self.cart.add_item(self.product3)

        actual = self.cart.get_total()
        self.assertEqual(70, actual)
