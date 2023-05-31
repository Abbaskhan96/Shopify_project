import unittest
#import pytest
import os
from dotenv import load_dotenv
import shopify
from shopify_functions import *
    
#client = Shopify.Session.Setup(api_key='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', secret='113702e4a88f0030c7fe324e0c20e5b5')
#Api key : ff468cda64e69c8e2a08e105af98fb1a


store_url="https://gfw-dev-1.myshopify.com/admin/api/2023-04"
access_token= "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"




session=shopify.Session(store_url, "2023-04", access_token)
shopify.ShopifyResource.activate_session(session)




class MainTestcases(unittest.TestCase):

    def setup(self):
        #authenting the Shopify with the token it is used in fixture
        #store_url="https://gfw-dev-1.myshopify.com/admin/api/2023-04"
        #access_token= "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"
        store_url= os.getenv('STORE URL')
        access_token= os.getenv('TOKEN')
        session=shopify.Session(store_url, "2023-04", access_token)
        shopify.ShopifyResource.activate_session(session)

    #Testing case for searching product in shopify
    def test_search_shopify_product(self):
        #List of product i want to search in shopify
        ask_input= input("Enter name of product you want to search: ")
        total_products_query=[]
        total_products_query= ["Carolina Rose Shrub","American Beautyberry Shrub"]
        total_products_query.append(ask_input)
        print(total_products_query)
        #calling the functions from the other Shopify_functions class file
        products= shopify_functions()
        products=products.search_products(total_products_query)
        print(products)

        #asserting the products from the shopify products finding it is correct or not
        self.assertIsInstance(products, list)
        self.assertEqual(len(products), len(total_products_query), f"Some Products are missing for query: '{total_products_query}'")
        self.assertTrue(all(isinstance(product, shopify.resources.Product) for product in products))
    


if __name__ == '__main__':
    unittest.main()






 
"""
# Test case for searching products
@pytest.mark.parametrize('query', ['plant', 'shirt'])
def test_search_products(query):
    products = search_products(query)
    assert isinstance(products, list)
    assert all(isinstance(product, shopify.resources.Product) for product in products)


# Example usage: running the tests
if __name__ == '__main__':
    pytest.main([__file__])
#@pytest.fixture(scope='session')

def shopify_client():
    return client


def test_search_product(shopify_client):
    # Search for products based on a keyword
    keyword = 'plants'
    products = shopify_client.Product.find(query=keyword)
    for product in products:
        assert keyword.lower() in product.title.lower()


def test_search_order(shopify_client):
    # Search for orders based on a keyword
    keyword = 'John Doe'
    orders = shopify_client.Order.find(query=keyword)
    for order in orders:
        assert keyword.lower() in f"{order.customer.first_name} {order.customer.last_name}".lower()

def test_create_order(shopify_client):
    # Create a new order
   s line_items = [(123456789, 2), (987654321, 1)]  # Variant IDs and quantities
    order = shopify_client.Order()
    for item in line_items:
        variant_id, quantity = item
        order.line_items.append({'variant_id': variant_id, 'quantity': quantity})
    order.save()
    assert order.id is not None


def test_check_order_response(shopify_client):
    # Check the response status of an order
    order_id = 123456789
    order = shopify_client.Order.find(order_id)
    assert order.financial_status == 'Paid'
"""

