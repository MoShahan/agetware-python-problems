# 4 - Problem: Minimizing Loss

import math


def main():
    n = int(input("Enter the number of years: "))  # to get number of years
    if n < 2:  # need minimum of 2 years to buy and sell
        print("Please enter minimum of 2 years")
        return
    prices = []
    for i in range(n):  # getting value for each year
        price = int(input(f"Enter the price for year {i + 1}: "))
        prices.append(price)

    buyYear = 0
    sellYear = 0
    minLoss = math.inf  # initializing minLoss to be infinity to compare later on

    for i in range(n):
        for j in range(i + 1, n):
            # if there is a loss AND current loss is lesser than whatever loss was saved before
            if (prices[j] - prices[i] < 0) and (minLoss > (prices[i] - prices[j])):
                minLoss = prices[i] - prices[j]
                buyYear = i
                sellYear = j

    if minLoss == math.inf:  # when there is no chance of loss in any combination
        print("No losses are available")
        return

    print("Buy Year:", buyYear + 1)
    print("Sell Year:", sellYear + 1)
    print(f"Minimum Loss: {prices[buyYear]} - {prices[sellYear]} = {minLoss}")


main()
