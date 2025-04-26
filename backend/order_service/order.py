from abc import ABC, abstractmethod

class Order(ABC):
    @abstractmethod
    def process_order(self):
        pass

class ElectronicOrder(Order):
    def process_order(self):
        return "Processing electronic item order"

class FurnitureOrder(Order):
    def process_order(self):
        return "Processing furniture item order"

class OrderFactory:
    def create_order(self, order_type: str) -> Order:
        if order_type == "electronic":
            return ElectronicOrder()
        elif order_type == "furniture":
            return FurnitureOrder()
        raise ValueError(f"Unknown order type: {order_type}")

# Порождающий паттерн: Абстрактная фабрика
class ProductFactory(ABC):
    @abstractmethod
    def create_product(self):
        pass

class ElectronicProductFactory(ProductFactory):
    def create_product(self):
        return {"name": "Smartphone", "category": "electronics"}

class FurnitureProductFactory(ProductFactory):
    def create_product(self):
        return {"name": "Sofa", "category": "furniture"}

def get_product_factory(category: str) -> ProductFactory:
    if category == "electronics":
        return ElectronicProductFactory()
    elif category == "furniture":
        return FurnitureProductFactory()
    else:
        raise ValueError(f"Unknown category: {category}")

# Поведенческий паттерн: Цепочка обязанностей
class OrderHandler(ABC):
    @abstractmethod
    def handle_order(self, order):
        pass

class PaymentHandler(OrderHandler):
    def handle_order(self, order):
        if order['payment_status'] != "paid":
            return "Order payment pending"
        return self.next_handler.handle_order(order)

class StockHandler(OrderHandler):
    def handle_order(self, order):
        if not order.get("in_stock", False):
            return "Product out of stock"
        return self.next_handler.handle_order(order)

class ShippingHandler(OrderHandler):
    def handle_order(self, order):
        return "Order is being shipped"

# Цепочка обязанностей
class OrderProcessingChain:
    def __init__(self):
        self.payment_handler = PaymentHandler()
        self.stock_handler = StockHandler()
        self.shipping_handler = ShippingHandler()

        # Связываем обработчики в цепочку
        self.payment_handler.next_handler = self.stock_handler
        self.stock_handler.next_handler = self.shipping_handler

    def process(self, order):
        return self.payment_handler.handle_order(order)

