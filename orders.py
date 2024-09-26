from clients import Client

class Order:
    def __init__(self, id, summ, date, Client):
        self.id = id
        self.summ = summ
        self.date = date
        self.status = None
        self.client = Client.name
        self.tel_number = Client.tel_number


    def get_status(self, status=0):
        return self.status

    def set_status(self, new_status):
        self.status = new_status

    def __str__(self):

        return f'id заказа {self.id}, дата заказа {self.date} , сумма заказа {self.summ} рублей, стату заказа {self.status}, клиент {self.client}, номер телефона клиента {self.tel_number}'

