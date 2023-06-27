def buy_and_sell_stocks(prices):
    profit = 0

    for i in range(len(prices)-1):
        if prices[i+1] > prices[i]:
            profit = profit + prices[i+1] - prices[i]

    return profit

prices = [7, 1, 5, 3, 6, 4]    # Return: 7
result = buy_and_sell_stocks(prices)
print(f"Profit: {result}")