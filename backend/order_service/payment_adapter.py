#Абстрактный класс. Метод будет переопределен в дочерних классах, чтобы реализовать свой собственный способ обработки платежа
class PaymentAdapter:
    def process_payment(self, amount):
        raise NotImplementedError
#Реализация для paypal
class PayPalPaymentAdapter(PaymentAdapter):
    def process_payment(self, amount):
        return f"Processed payment of {amount} via PayPal"
#Реализация для credit card
class CreditCardPaymentAdapter(PaymentAdapter):
    def process_payment(self, amount):
        return f"Processed payment of {amount} via Credit Card"
# порождающий паттерн "Фабричный метод". принимаем цену и метод оплаты. создаем адаптер под метод, если не совпадает с нашими, то выдаем ошибку.
def process_order_payment(amount, payment_method: str):
    if payment_method == "paypal":
        adapter = PayPalPaymentAdapter()
    elif payment_method == "creditcard":
        adapter = CreditCardPaymentAdapter()
    else:
        raise ValueError("Unknown payment method")
    
    return adapter.process_payment(amount)
