def max_stock_profit(prices):
    """ """

    min_price_seen = float('inf')
    max_profit = 0

    # keep track of the min price
    # keep track of the max difference
    for price in prices:
        profit_today = price - min_price_seen
        max_profit = max(max_profit, price - min_price_seen)
        min_price_seen = min(min_price_seen, price)
        
    return max_profit




prices = [7,1,5,3,6,4]
# 5
print(max_stock_profit(prices))