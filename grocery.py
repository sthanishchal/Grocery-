items = {'apple': 0.50, 'banana': 0.25, 'bread': 1.99, 'milk': 2.49, 'eggs': 1.99}

order_list = []
total_cost = 0

print('Welcome to our grocery store!')
print('Menu:')
for item, price in items.items():
    print(f'{item}: Rs{price:.2f}')

while True:
    item = input('What would you like to order? ').lower()
    
    if item not in items:
        print('Sorry, we do not have that item.')
        continue
    
    quantity = int(input(f'How many {item}(s) would you like? '))
    
    order_list.append((item, quantity))
    
    total_cost += quantity * items[item]
    
    cont = input('Would you like to keep ordering? (y/n) ').lower()
    
    if cont != 'y':
        break

print('Your order:')
for item, quantity in order_list:
    print(f'{quantity} {item}(s)')
print(f'Total cost: ${total_cost:.2f}')
