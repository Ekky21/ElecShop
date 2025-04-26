import unittest
from product_service.product import ProductService, GridDisplayStrategy, ListDisplayStrategy, SingleProduct, ProductBundle

class TestProductService(unittest.TestCase):
    def test_grid_display_strategy(self):
        service = ProductService(GridDisplayStrategy())
        product = {"name": "Smartphone"}
        self.assertEqual(service.display_product(product), "Displaying Smartphone in grid format")
    
    def test_list_display_strategy(self):
        service = ProductService(ListDisplayStrategy())
        product = {"name": "Smartphone"}
        self.assertEqual(service.display_product(product), "Displaying Smartphone in list format")

    def test_product_bundle(self):
        product1 = SingleProduct("Smartphone", 500)
        product2 = SingleProduct("Headphones", 100)

        bundle = ProductBundle()
        bundle.add(product1)
        bundle.add(product2)
        self.assertEqual(bundle.get_price(), 600)

if __name__ == '__main__':
    unittest.main()
