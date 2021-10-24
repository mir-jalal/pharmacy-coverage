class Product(object):
    def __init__(self, product_code, name, subtitle, description, price):
        self.name = name
        self.product_code = product_code
        self.subtitle = subtitle
        self.description = description
        self.price = price
        self.quantity = 0
        self.tags = []

    def increase_quantity(self):
        self.quantity += 1

    def decrease_quantity(self):
        if self.quantity > 0:
            self.quantity -= 1

    def add_tag(self, tag_name):
        if tag_name not in self.tags:
            self.tags.append(tag_name)
            return True
        else:
            return False

    def remove_tag(self, tag_name):
        if tag_name in self.tags:
            self.tags.remove(tag_name)
            return True
        else:
            return False

    def get_tags(self):
        return self.tags

    def clear_tags(self):
        while self.tags:
            self.tags.pop(0)
