class Product:
    sku = 0
    
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category
        Product.sku += 1
        self.sku = f'sku00{Product.sku}'
        
    def update_price(self, percent_change, is_increased):
        if is_increased:
            self.price *= ((100 + percent_change) / 100)
        else:
            self.price *= ((100 - percent_change) / 100)
        return self

    def print_info(self):
        print(f'Product {self.name} ({self.sku}):\n category:{self.category}\n price:{self.price}\n')
        return self
