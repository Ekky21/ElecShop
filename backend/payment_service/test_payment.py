import unittest
from payment_service.payment import PaymentService, PayPalPayment, CreditCardPayment

class TestPaymentService(unittest.TestCase):
    def test_paypal_payment(self):
        service = PaymentService(PayPalPayment())
        self.assertEqual(service.process_payment(100), "Processed payment of 100 via PayPal")
    
    def test_creditcard_payment(self):
        service = PaymentService(CreditCardPayment())
        self.assertEqual(service.process_payment(200), "Processed payment of 200 via Credit Card")

if __name__ == '__main__':
    unittest.main()
