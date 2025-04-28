import unittest
from payment_service.payment import PaymentService, PayPalPayment, CreditCardPayment, DiscountPaymentDecorator
#unittest.TestCase - базовый класс, предоставляет базовые методы для тестов
class TestPaymentService(unittest.TestCase):
    def test_paypal_payment(self):
        service = PaymentService(PayPalPayment())
        self.assertEqual(service.process_payment(100), "Processed payment of 100 via PayPal")
    
    def test_creditcard_payment(self):
        service = PaymentService(CreditCardPayment())
        self.assertEqual(service.process_payment(200), "Processed payment of 200 via Credit Card")

    def test_discount_decorator(self):
        # Тестируем применение скидки к платежу
        payment_service = PayPalPayment()
        payment_service_with_discount = DiscountPaymentDecorator(payment_service, 0.1)  # 10% скидка
        result = payment_service_with_discount.process_payment(100)
        self.assertEqual(result, "Processed payment of 90.0 via PayPal")  # Платеж должен быть 90 (100 - 10%)

    def test_credit_card_with_discount(self):
        # Тестируем оплату через кредитную карту с применением скидки
        payment_service = CreditCardPayment()
        payment_service_with_discount = DiscountPaymentDecorator(payment_service, 0.2)  # 20% скидка
        result = payment_service_with_discount.process_payment(150)
        self.assertEqual(result, "Processed payment of 120.0 via Credit Card")  # Платеж должен быть 120 (150 - 20%)
if __name__ == '__main__':
    unittest.main()
