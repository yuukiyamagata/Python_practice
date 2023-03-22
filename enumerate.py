prices = [100, 200, 300]

quantities = [1,2,3,4,5]

for(price, quantity) in zip(prices, quantities):
    print(price*quantity)

menu=["coffee", "tea", "cake", "ice_cream"]


for(item, price, quantity) in zip(menu, prices, quantities):
    print(item, price*quantity)