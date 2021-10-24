from product import Product


class Cart(object):
    def __init__(self):
        self.items = []

    def add_item(self, item: Product):
        if item.quantity < 1:
            return False

        found = False

        for index, i in enumerate(self.items):
            if item.product_code == i.product_code:
                self.items[index].quantity += item.quantity
                found = True

        if not found:
            self.items.append(item)

        return True

    def remove_item(self, item: Product):
        if item.quantity < 1:
            return False

        found = False

        for index, i in enumerate(self.items):
            if item.product_code == i.product_code:
                if self.items[index].quantity > item.quantity:
                    self.items[index].quantity -= item.quantity
                else:
                    self.items.remove(item)
                return True

        if not found:
            return False

    def get_total(self):
        total = 0

        for item in self.items:
            total += item.quantity * item.price

        return total
