import shopify

class shopify_functions:
    #this function is used to search the products the product list will be given from the main test file
    def search_products(self,total_products_query):
        
        #creating empty list for all response adding from Shopify then it will returen the list of finded products
        products = []
        #finding all the products provided by the list
        for title in total_products_query:
            products += shopify.Product.find(title=title)
        #printing each product info by following loop
        for product in products:
            print(f"Product ID: {product.id}")
            print(f"Title: {product.title}")
            print(f"Vendor: {product.vendor}")
            print(f"Type: {product.product_type}")
            print(f"Created At: {product.created_at}")
            print(f"Updated At: {product.updated_at}")
            print(f"Published Scope: {product.published_scope}")
            print(f"Status: {product.status}")
            print(f"Tags: {product.tags}")
            print(f"Variants: {len(product.variants)}")
            print('---------------')
        #returning the final list of response products
        return products