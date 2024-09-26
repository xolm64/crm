from clients import Client
from WashingFactory import WashingFactory
from orders import Order

WashingFactorySaratov= WashingFactory('Саратовская фабрика стирки ковров')

Vasy = Client('Vasy', "89270505050", 'Saratov, street Lenina d.2')
Vadim = Client('Vadim', "89270505051", 'Saratov, street Main d.5')
Igor = Client('Igor', "89270505052", 'Saratov, street Kirova d.3')

order1 = Order(1, 1500, '2024-02-01', Vasy)
order2 = Order(2, 2500, '2024-02-02', Vadim)
order3 = Order(3, 3500, '2024-02-03', Igor)

WashingFactorySaratov.add_order(order1)
WashingFactorySaratov.add_order(order2)
WashingFactorySaratov.add_order(order3)


WashingFactorySaratov.all_orders_in_factory()
WashingFactorySaratov.add_archive(order2)
print("++++++++++++++++++++++++++++++++++")
WashingFactorySaratov.all_orders_in_factory()



main_menu = ("\nМеню:\n"
             "1. Показать заказы в работе на фабрике\n"
             "2. Добавить новый заказ\n"
             "3. Заказ выполнен. Перенести заказ в архив\n"
             "4. Показать список выполненых заказов-Архив\n"
             "5. Поиск заказа\n"
             "q. Выход")
while True:

    print(main_menu)

    user_input = input("Ваш выбор: ")

    if user_input == "1":
        print("Показать заказы в работе на фабрике")
        WashingFactorySaratov.all_orders_in_factory()
    elif user_input == "2":
        print("Вы выбрали: добавить новый заказ")
    elif user_input == '3':
        print("Вы выбрали: Заказ выполнен. Перенести заказ в архив")
        WashingFactorySaratov.all_orders_in_factory()
        id_order = input("укажите id заказа, который надо перенести в архив")

        WashingFactorySaratov.add_archive()


    elif user_input == '4':
        print("Вы выбрали: Показать список выпоненых заказов - Архив ")
        WashingFactorySaratov.orders_archive()
    elif user_input == "5":
        print("Вы выбрали: Поиск заказа по номеру телефона клиента")

        tel_find = str(input('Введите номер телефона клиента '))
        for elem in WashingFactorySaratov.orders:
             if tel_find in str(elem):
                 print(elem)
             else:
                 pass
        print(" поиск завершен")



    elif user_input == 'q':
        break