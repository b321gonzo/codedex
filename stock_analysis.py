# Stonks 
# Codédex

#$AMC stock from 11/1/2022 to 11/21/2022 (weekdays only). Here are the stock prices (in dollars) for each of these days:
stock_prices = [ 6.15, 5.81, 5.70, 5.65, 5.33, 5.62, 5.19, 6.13, 7.20, 7.34, 7.95, 7.53, 7.39, 7.59, 7.27 ]


def max_price(a,b):
    stock_range=list()
    for i in range(a-1,b):
        stock_range.append(stock_prices[i])
    return max(stock_range)

def min_price(a,b):
    stock_range=list()
    for i in range(a-1,b):
        stock_range.append(stock_prices[i])
    return min(stock_range)

def price_at(x):
    return stock_prices[x-1]

print(max_price(5,7))
print(min_price(3,6))
print(price_at(1))
print(price_at(8))
print(price_at(15))