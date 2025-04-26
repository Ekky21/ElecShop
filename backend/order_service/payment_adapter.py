class PaymentAdapter:
    def process_payment(self, amount):
        raise NotImplementedError

class PayPalPaymentAdapter(PaymentAdapter):
    def process_payment(self, amount):
        return f"Processed payment of {amount} via PayPal"

class CreditCardPaymentAdapter(PaymentAdapter):
    def process_payment(self, amount):
        return f"Processed payment of {amount} via Credit Card"

def process_order_payment(amount, payment_method: str):
    if payment_method == "paypal":
        adapter = PayPalPaymentAdapter()
    elif payment_method == "creditcard":
        adapter = CreditCardPaymentAdapter()
    else:
        raise ValueError("Unknown payment method")
    
    return adapter.process_payment(amount)
