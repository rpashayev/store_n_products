from classes.product import Product
from classes.store import Store

# create Store instance
first_store = Store('RG store')

# create Product instances
product1 = Product('HP laptop', 1199, 'electronics')
product2 = Product('Acer mouse', 25, 'accessories')
product3 = Product('Acer keyboard', 89, 'accessories')
product4 = Product('HP display', 199, 'displays')
product5 = Product('Dell laptop', 1099, 'electronics')
product6 = Product('Apple laptop', 1899, 'electronics')
product7 = Product('Samsung display', 219, 'displays')

# add Product to Store - invoke add_product() method of the Store class
first_store.add_product(product1)
first_store.add_product(product2)
first_store.add_product(product3)
first_store.add_product(product4)
first_store.add_product(product5)
first_store.add_product(product6)
first_store.add_product(product7)

# invoke print_info() method of the Product class
for p in first_store.products_list:
    p.print_info()


# invoke update_price() method of the Product class - update "Apple laptop" product price only
for prod in first_store.products_list:
    if prod.name == 'Apple laptop':
            prod.update_price(5, False)

# invoke print_info() method of Product class to check if price is updated
print(f'------------\nDiscounted prices')
for p in first_store.products_list:
    p.print_info()

# invoke sell_product() of the Store class
print(f'------------\nSold product:\n------------')
first_store.sell_product('sku003')
print(f'------------\nNew list of the products:\n------------')
for p in first_store.products_list:
    p.print_info()

# invoke inflation() of the Store class - 3%
first_store.inflation(3)
print(f'------------\nNew prices after 3% inflation:\n------------')
for p in first_store.products_list:
    p.print_info()
    
# invoke set_clearance() of the Store class
first_store.set_clearance('displays',10)
print(f'------------\nClearance prices - Displays 10%:\n------------')
for p in first_store.products_list:
    p.print_info()
