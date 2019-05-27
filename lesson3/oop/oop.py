
class Point(object):

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def coordinates(self):
        return "Coordinates are: x = {}, y = {}".format(self.x, self.y)

    def __repr__(self):
        return "Point: x = {}, y = {}".format(self.x, self.y)


class Product(object):

    def __init__(self, name, price, stock=0, discount=0, max_discount=20):
        self.name = name.strip()
        if len(self.name) < 2:
            raise ValueError("Product name has to be at least 2 words")
        self.price = abs(float(price))
        self.stock = abs(int(stock))
        self.discount = abs(float(discount))
        self.max_discount = abs(float(max_discount))

        if self.max_discount > 99:
            raise ValueError("Too big max discount")

        if self.discount > self.max_discount:
            self.discount = self.max_discount

    def discounted(self):
        return self.price - self.price * self.discount / 100

    def __repr__(self):
        return "Product name: {}, price: {}, stock: {}".format(self.name, self.price, self.stock)

    def sell(self, items_count):
        self.items_count = abs(int(items_count))
        if self.items_count > self.stock:
            raise ValueError("Not enough items on the stock")
        else:
            self.stock -= self.items_count

class Phone(Product):
    def __init__(self, name, price, color, stock=0, discount=0, max_discount=20):
        super().__init__(name, price, stock, discount, max_discount)
        self.color = color
        if type(self.color) != str:
            raise ValueError("Color has to be a string type")

    def __repr__(self):
        print(super())
        return "Phone name: {}, price: {}, stock: {}".format(self.name, self.price, self.stock, self.color)

    def get_color(self):
        return "Color: {}".format(self.color)

class Sofa(Product):
    def __init__(self, name, price, color, texture, stock=0, discount=0, max_discount=20):
        super().__init__(name, price, stock, discount, max_discount)
        self.color = color
        self.texture = texture
        if type(self.color) != str:
            raise ValueError("Color has to be a string type")

        if type(self.texture) != str:
            raise ValueError("Texture has to be a string type")


    def __repr__(self):
        print(super())
        return "Sofa name: {}, price: {}, stock: {}, color: {}, texture: {}".format(self.name, self.price, self.stock, self.color, self.texture)

    def get_size(self):
        raise NotImplementedError("Sorry! This method didn't implemented yet :(")


phone1 = Phone('Xiaomi Mi A10', 25000, "grey")
print(phone1)
print(phone1.get_color())


sofa1 = Sofa('Divan', 15000, color="grey", texture="rombik")
print(sofa1)


sofa1.get_size()


