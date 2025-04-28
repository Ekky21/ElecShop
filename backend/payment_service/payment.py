#Модуль для обработки платежей
from abc import ABC, abstractmethod
#abc - родитель (шаблон) для классов. abstractmethod - позволяет изменять поведение функций с помощью изменения функциональности без изменения кода.
#абстрактный класс. принимаем сумму платежа и возвращаем строку, как был обработан платеж
#Поведенческий паттерн "Стратегия"
class PaymentStrategy(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass
# реализация класса, выводим что оплата прошла через paypal
class PayPalPayment(PaymentStrategy):
    def process_payment(self, amount):
        return f"Processed payment of {amount} via PayPal"
# реализация класса, выводим что оплата прошла через credit card
class CreditCardPayment(PaymentStrategy):
    def process_payment(self, amount):
        return f"Processed payment of {amount} via Credit Card"
#класс, использующий выбранную стратегию для обработки платежей.

#Структурный паттерн "декоратор" для расширения функциональности
class PaymentDecorator(ABC):
    def __init__(self, payment):
        self._payment = payment

    @abstractmethod
    def process_payment(self, amount):
        pass

# Класс для добавления скидки
class DiscountPaymentDecorator(PaymentDecorator):
    def __init__(self, payment, discount):
        super().__init__(payment) # конструктор родительского класса paymentdecorator, чтобы сохранить объект стратегии
        self.discount = discount #величина скидки

    def process_payment(self, amount): #расчет скидки
        discounted_amount = amount * (1 - self.discount)
        return self._payment.process_payment(discounted_amount)
class PaymentService:
    def __init__(self, strategy: PaymentStrategy):
        self.strategy = strategy
    #метод, позволяющий сменить стратегию оплаты в процессе работы.
    def set_payment_strategy(self, strategy: PaymentStrategy):
        self.strategy = strategy
   #метод, использующий текущую стратегию для обработки платежа.
    def process_payment(self, amount):
        return self.strategy.process_payment(amount)
