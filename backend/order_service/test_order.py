import unittest
from order_service.order import OrderFactory, OrderProcessingChain

class TestOrderService(unittest.TestCase):
    def test_create_electronic_order(self):
        factory = OrderFactory()
        order = factory.create_order("electronic")
        self.assertEqual(order.process_order(), "Processing electronic item order")
    
    def test_create_furniture_order(self):
        factory = OrderFactory()
        order = factory.create_order("furniture")
        self.assertEqual(order.process_order(), "Processing furniture item order")

    def test_order_processing_chain(self):
        order = {"payment_status": "paid", "in_stock": True}
        chain = OrderProcessingChain()
        self.assertEqual(chain.process(order), "Order is being shipped")

if __name__ == '__main__':
    unittest.main()
