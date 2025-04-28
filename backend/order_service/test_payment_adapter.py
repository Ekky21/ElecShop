# test_payment_adapter.py

import unittest
from payment_adapter import PayPalPaymentAdapter, CreditCardPaymentAdapter, PaymentAdapter


class TestPaymentAdapter(unittest.TestCase):

    def test_paypal_payment(self):
        # Тестируем PayPalPaymentAdapter
        paypal_adapter = PayPalPaymentAdapter()
        result = paypal_adapter.process_payment(100)
        self.assertEqual(result, "Processed payment of 100 via PayPal")

    def test_creditcard_payment(self):
        # Тестируем CreditCardPaymentAdapter
        credit_card_adapter = CreditCardPaymentAdapter()
        result = credit_card_adapter.process_payment(200)
        self.assertEqual(result, "Processed payment of 200 via Credit Card")

    def test_process_payment_invalid_method(self):
        # Тестируем что происходит, если вызываем процесс без реализации
        with self.assertRaises(NotImplementedError):
            adapter = PaymentAdapter()
            adapter.process_payment(100)  # Этот вызов должен вызвать ошибку, так как PaymentAdapter абстрактный класс
