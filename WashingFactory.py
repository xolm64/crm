

class WashingFactory:
    def __init__(self, name):
        self.name = name
        self.orders = []
        self.orders_archive = []
    def add_order(self, new_order):
        new_order.set_status(True)
        self.orders.append(new_order)

    def add_archive(self, order):
        order.set_status(False)
        self.orders_archive.append(order)

    def all_orders_in_factory(self):
        for order in self.orders:
            print(order)
    def orders_archive(self):
        for order in self.orders_archive:
            print(order)

    def find_order(self, tel_number):
        pass

