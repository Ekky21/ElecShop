from abc import ABC, abstractmethod

class ProductDisplayStrategy(ABC):
    @abstractmethod
    def display_product(self, product):
        pass

class GridDisplayStrategy(ProductDisplayStrategy):
    def display_product(self, product):
        return f"Displaying {product['name']} in grid format"

class ListDisplayStrategy(ProductDisplayStrategy):
    def display_product(self, product):
        return f"Displaying {product['name']} in list format"

# Структурный паттерн: Компоновщик
class ProductComponent(ABC):
    @abstractmethod
    def get_price(self) -> float:
        pass

class SingleProduct(ProductComponent):
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price
    
    def get_price(self) -> float:
        return self.price

class ProductBundle(ProductComponent):
    def __init__(self):
        self.components = []
    
    def add(self, component: ProductComponent):
        self.components.append(component)
    
    def get_price(self) -> float:
        return sum(component.get_price() for component in self.components)

# Пример использования:
product1 = SingleProduct("Smartphone", 500)
product2 = SingleProduct("Headphones", 100)

bundle = ProductBundle()
bundle.add(product1)
bundle.add(product2)

print(bundle.get_price())  # Выведет 600
