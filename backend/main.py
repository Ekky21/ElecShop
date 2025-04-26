from order_service.order import OrderFactory
from payment_service.payment import PaymentService, PayPalPayment
from product_service.product import ProductService, GridDisplayStrategy

# Пример создания заказа
factory = OrderFactory()
order = factory.create_order("electronic")
print(order.process_order())  # Выводит информацию о заказе

# Пример обработки платежа
payment_service = PaymentService(PayPalPayment())
print(payment_service.process_payment(100))  # Выводит информацию о платеже

# Пример отображения товара
product_service = ProductService(GridDisplayStrategy())
product = {"name": "Smartphone"}
print(product_service.display_product(product))  # Выводит товар в виде сетки
