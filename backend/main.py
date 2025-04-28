from product_service.product import ProductService, GridDisplayStrategy, ListDisplayStrategy, SingleProduct, ProductBundle
from payment_service.payment import PaymentService, PayPalPayment

# Создаем объект стратегии для отображения товара в сетке
service = ProductService(GridDisplayStrategy())

# Создаем объект товара
product = SingleProduct("Smartphone", 500)

# Теперь передаем объект товара
print(service.display_product(product))  # Выведет: "Displaying Smartphone in grid format"

# Создаем второй товар
product2 = SingleProduct("Headphones", 100)

# Создаем комплект товаров
bundle = ProductBundle()
bundle.add(product)
bundle.add(product2)

# Выводим цену комплекта
print(f"Total price of bundle: ${bundle.get_price()}")  # Выведет 600

# Создание и использование метода для платежей (пример)
payment_service = PaymentService(PayPalPayment())  # Используем PayPal для платежа
print(payment_service.process_payment(bundle.get_price()))  # Выведет: "Processed payment of 600 via PayPal"
