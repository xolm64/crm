

class Client:
    def __init__(self, name, tel_number, address):
        self.name = name
        self.tel_number = tel_number
        self.address = address
    def __str__(self):
        return f'Клиент {self.name} ,  номер телефона {self.tel_number}, адрес {self.address}'



