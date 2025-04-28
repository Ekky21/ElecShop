import unittest
from order import OrderFactory, OrderProcessingChain


class TestOrderFactorySingleton(unittest.TestCase):

    def test_singleton_factory(self):
        # Создаем два экземпляра фабрики
        factory1 = OrderFactory()
        factory2 = OrderFactory()

        # Проверяем, что оба экземпляра ссылаются на один и тот же объект
        self.assertIs(factory1, factory2, "OrderFactory is not a singleton")


class TestOrderProcessingChain(unittest.TestCase):

    def test_order_processed_successfully(self):
        # Создаем фабрику и заказ
        factory = OrderFactory()
        order = factory.create_order()  # Создаем заказ на электронные товары
        order.items = ["Smartphone", "Headphones"]
        order.payment_status = "paid"

        # Создаем цепочку для обработки заказа
        chain = OrderProcessingChain()

        # Обрабатываем заказ
        result = chain.process(order)

        # Проверяем, что заказ был отправлен
        self.assertEqual(result, "Order is being shipped")

    def test_order_payment_pending(self):
        # Создаем фабрику и заказ
        factory = OrderFactory()
        order = factory.create_order()  # Создаем заказ на электронные товары
        order.items = ["Smartphone", "Headphones"]
        order.payment_status = "unpaid"  # Статус оплаты "не оплачен"

        # Создаем цепочку для обработки заказа
        chain = OrderProcessingChain()

        # Обрабатываем заказ
        result = chain.process(order)

        # Проверяем, что заказ не был отправлен из-за неуплаты
        self.assertEqual(result, "Order payment pending")

    def test_product_out_of_stock(self):
        # Создаем фабрику и заказ
        factory = OrderFactory()
        order = factory.create_order()  # Создаем заказ на электронные товары
        order.items = []  # Пустой список товаров (товара нет на складе)
        order.payment_status = "paid"

        # Создаем цепочку для обработки заказа
        chain = OrderProcessingChain()

        # Обрабатываем заказ
        result = chain.process(order)

        # Проверяем, что заказ не был отправлен из-за отсутствия товара
        self.assertEqual(result, "Product out of stock")
