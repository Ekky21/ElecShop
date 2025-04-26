from abc import ABC, abstractmethod

class PaymentStrategy(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

class PayPalPayment(PaymentStrategy):
    def process_payment(self, amount):
        return f"Processed payment of {amount} via PayPal"

class CreditCardPayment(PaymentStrategy):
    def process_payment(self, amount):
        return f"Processed payment of {amount} via Credit Card"

class PaymentService:
    def __init__(self, strategy: PaymentStrategy):
        self.strategy = strategy
    
    def set_payment_strategy(self, strategy: PaymentStrategy):
        self.strategy = strategy
    
    def process_payment(self, amount):
        return self.strategy.process_payment(amount)
