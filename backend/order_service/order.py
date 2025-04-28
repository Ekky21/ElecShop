#Модуль для работы с заказами
from abc import ABC, abstractmethod
#abc - родитель (шаблон) для классов. abstractmethod - позволяет изменять поведение функций с помощью изменения функциональности без изменения кода.
#абстрактный класс для всех заказов. process_order - возвращает строку обрабатывается ли заказ
class Order(ABC):
    @abstractmethod
    def process_order(self):
        pass
#конкретная реализация на электронные товары
class ElectronicOrder(Order):
    def __init__(self):
        self.items = []
        self.payment_status = "unpaid"
    def process_order(self):
        return "Processing electronic item order"

# Порождающий паттерн" Одиночка" (синглтон) для создания заказов ( один экземпляр фабрики)
class OrderFactory:
    _instance = None

    def __new__(cls): #будет создан только один экземпляр ( если он есть, то будет возвращен снова)
        if cls._instance is None:
            cls._instance = super(OrderFactory, cls).__new__(cls)
        return cls._instance

    def create_order(self) -> Order: #создаем заказ на товар
        return ElectronicOrder()

# Поведенческий паттерн: Цепочка обязанностей
class OrderHandler(ABC):
    @abstractmethod
    def handle_order(self, order): #каждый обработчик будет реализовывать свою логику обработки заказа
        pass
class StockHandler(OrderHandler):
    def handle_order(self, order):
        # Проверка наличия товаров на складе
        if not order.items:  # Если товара нет на складе
            return "Product out of stock"
        return self.next_handler.handle_order(order)

class PaymentHandler(OrderHandler): #был ли заказ оплачен (если все успешно, то передаем дальше)
    def handle_order(self, order):
        # Проверка статуса оплаты
        if order.payment_status != "paid":
            return "Order payment pending"
        return self.next_handler.handle_order(order)

class ShippingHandler(OrderHandler): #выполняем этап отправки товара
    def handle_order(self, order):
        # Если все проверки пройдены, товар отправляется
        return "Order is being shipped"

# Цепочка обязанностей
class OrderProcessingChain:
    def __init__(self):
        self.stock_handler = StockHandler()
        self.payment_handler = PaymentHandler()
        self.shipping_handler = ShippingHandler()

        # Связываем обработчики в цепочку
        self.stock_handler.next_handler = self.payment_handler #после проверки наличия передаем на оплату
        self.payment_handler.next_handler = self.shipping_handler # если оплачено, то отправляем товар

    def process(self, order): #выполняем обработку заказа
        return self.stock_handler.handle_order(order)


