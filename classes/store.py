from . import product
class Store:
    def __init__(self, name):
        self.name = name
        self.products_list = []
        
    def add_product(self, new_product):
        self.products_list.append(new_product)
        return self
    
    def sell_product(self, sku):
        for prod in self.products_list:
            if prod.sku == sku:
                prod.print_info()
                self.products_list.remove(prod)
        return self
    
    def inflation(self, percent_increase):
        is_increase = True
        for prod in self.products_list:
            prod.update_price(percent_increase, is_increase)
        return self
    
    def set_clearance(self, category, percent_discount):
        is_increase = False
        for prod in self.products_list:
            if prod.category == category:
                prod.update_price(percent_discount, is_increase)
        return self