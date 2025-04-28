import unittest
from product_service.product import ProductService, GridDisplayStrategy, ListDisplayStrategy, SingleProduct, \
    ProductBundle

#unittest.TestCase - базовый класс, предоставляет базовые методы для тестов
class TestProductService(unittest.TestCase):

    def test_grid_display_strategy(self):
        # Используем стратегию отображения в виде сетки
        service = ProductService(GridDisplayStrategy())

        # Создаем продукт
        product = SingleProduct("Smartphone", 500)

        # Проверяем, что продукт правильно отображается в виде сетки
        self.assertEqual(service.display_product(product), "Displaying Smartphone in grid format")

    def test_list_display_strategy(self):
        # Используем стратегию отображения в виде списка
        service = ProductService(ListDisplayStrategy())

        # Создаем продукт
        product = SingleProduct("Smartphone", 500)

        # Проверяем, что продукт правильно отображается в виде списка
        self.assertEqual(service.display_product(product), "Displaying Smartphone in list format")

    def test_product_bundle(self):
        # Создаем два одиночных продукта
        product1 = SingleProduct("Smartphone", 500)
        product2 = SingleProduct("Headphones", 100)

        # Создаем комплект товаров
        bundle = ProductBundle()
        bundle.add(product1)
        bundle.add(product2)

        # Проверяем, что цена комплекта правильная
        self.assertEqual(bundle.get_price(), 600)


if __name__ == '__main__':
    unittest.main()
