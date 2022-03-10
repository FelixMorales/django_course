from store.models import Product

class ProductService:
    def get_in_stock(self):
        return Product.manager.get_in_stock()

    def find_by_category(self, category_name: str):        
        return Product.manager.find_by_category(category_name=category_name)

    def filter(self, name, category, only_in_stock, order_by):    
        return Product.manager.find_by_values(name=name, category=category, only_in_stock=only_in_stock, order_by=order_by)
