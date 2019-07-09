def maxProfit(prices):
    maxProfit = prices[1] - prices[0]
    maxPrice = prices[0]
    minPrice = prices[0]
    for price in range(1, len(prices)):
        current_price = prices[price]
        minPrice = min(minPrice, current_price)
        potential_profit = current_price - minPrice
        maxProfit = max(maxProfit, potential_profit)
    return maxProfit


print(maxProfit([7, 1, 5, 3, 6, 4]))
print(maxProfit([7, 6, 4, 3, 1]))
