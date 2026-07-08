arr = [7,1,5,3,6,4]

def StockBuyAndSell(arr):
    min_price = float('inf')
    max_profit = 0

    for i in range(len(arr)):
        if arr[i] < min_price:
            min_price = arr[i]
        else:
            max_profit = max(max_profit, arr[i] - min_price)

    return max_profit


print(StockBuyAndSell(arr))