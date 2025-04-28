#Модуль для работы с товарами
from abc import ABC, abstractmethod
#abc - родитель (шаблон) для классов. abstractmethod - позволяет изменять поведение функций с помощью изменения функциональности без изменения кода.

#Поведенческий паттерн "Стратегия" для отображения товара. Задает интерфейс для всех стратегий отображения товара (список, сетка)
#self каждый объект свое индивидуальное значение атрибута
class ProductDisplayStrategy(ABC):
    @abstractmethod
    def display_product(self, product):
        pass
#каждый объект выводится определенным образом.

class GridDisplayStrategy(ProductDisplayStrategy): #отображения товара в виде сетки
    def display_product(self, product):
        return f"Displaying {product.name} in grid format"


class ListDisplayStrategy(ProductDisplayStrategy): #отображения товара в виде списка
    def display_product(self, product):
        return f"Displaying {product.name} in list format"


# Структурный паттерн "Компоновщик" для работы с одиночными продуктами и наборами продуктов одинаково
#Возвращаем цену продукта методом get_price
class ProductComponent(ABC):
    @abstractmethod
    def get_price(self) -> float:
        pass
#каждый объект возвращает цену.
#для одиночных. есть имя, цена. возвращаем цену
#init инизиализируем объект (устанавливаем начальных значений атрибутов)
class SingleProduct(ProductComponent):
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def get_price(self) -> float:
        return self.price

# Класс для комплекта товаров. Суммируем все цены в заказе
class ProductBundle(ProductComponent):
    def __init__(self):
        self.components = []

    def add(self, component: ProductComponent):
        self.components.append(component)

    def get_price(self) -> float:
        return sum(component.get_price() for component in self.components)


# Новый класс ProductService для использования паттерна "Стратегия". принимает стратегию отображения и использует для отображения товаров.
class ProductService:
    def __init__(self, strategy: ProductDisplayStrategy):
        self.strategy = strategy

    def set_display_strategy(self, strategy: ProductDisplayStrategy):
        self.strategy = strategy

    def display_product(self, product):
        return self.strategy.display_product(product)
