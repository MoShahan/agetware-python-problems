# 4 - Problem: Minimizing Loss

import math


def main():
    n = int(input("Enter the number of years: "))
    prices = []
    for i in range(n):
        price = int(input(f"Enter the price for year {i + 1}: "))
        prices.append(price)

    buyYear = 0
    sellYear = 0
    minLoss = math.inf

    for i in range(n):
        for j in range(i + 1, n):
            if (prices[j] - prices[i] < 0) and (minLoss > (prices[i] - prices[j])):
                minLoss = prices[i] - prices[j]
                buyYear = i
                sellYear = j

    print("Buy Year:", buyYear + 1)
    print("Sell Year:", sellYear + 1)
    print(f"Minimum Loss: {prices[buyYear]} - {prices[sellYear]} = {minLoss}")


main()
