# lesson learned - when might think an O(n^2) is necessary, see if you can
# simply hold onto the current comparable value, and go down to O(n)

def max_stock_profit(prices):
    """Take in list of stock prices, return max profit possible from 1 trade
    
    >>> max_stock_profit([7,1,5,3,6,4])
    5
    >>> max_stock_profit([2,3])
    1
    """

    min_price_seen = float('inf')
    max_profit = 0

    for price in prices:
        profit_today = price - min_price_seen
        max_profit = max(max_profit, profit_today)
        min_price_seen = min(min_price_seen, price)

    return max_profit


if __name__ == "__main__":
    import doctest
    if doctest.testmod():
        print("max profit!")