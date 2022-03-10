from django.db import models

class ProductQuerySet(models.QuerySet):
    def in_stock(self):
        return self.filter(stock_count__gt=0)
    
    def by_category(self, name):
        return self.filter(stock_count__gt=0, categories__name=name)
    
    def fetch_images(self):
        return self.prefetch_related('images')

class ProductManager(models.Manager):
    
    def get_queryset(self):
        return ProductQuerySet(self.model, using=self._db)

    def get_in_stock(self):
        query_set = self.get_queryset()
        return query_set.in_stock().order_by('price')
    
    def find_by_category(self, category_name):
        result = self.get_queryset().by_category(name=category_name).fetch_images()
        return result

    def find_by_values(self, name, category, only_in_stock, order_by):
        filters = {}

        if name:
            filters['name__icontains'] = name
            
        if category:
            filters['categories'] = category
        
        if only_in_stock:
            filters['stock_count__gt'] = 0
            
        result = self.get_queryset().filter(**filters)

        if order_by == "NAME":
            result = result.order_by('name')
        
        if order_by == "PRICE_ASC":
            result = result.order_by('price')
        
        if order_by == 'PRICE_DESC':
            result = result.order_by('price').reverse()
        
        return result.fetch_images()
        
        

        


