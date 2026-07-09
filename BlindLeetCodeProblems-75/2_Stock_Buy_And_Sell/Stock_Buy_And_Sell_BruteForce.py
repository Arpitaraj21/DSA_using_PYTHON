arr = [7,1,5,3,6,4]


def StockBuyAndSell(arr):
    maximum = 0
    for i in range(len(arr)):
      for j in range(i+1, len(arr)):
        
        max_profit = arr[j] - arr[i]
        if max_profit > maximum:
            maximum = max_profit
    
    return maximum


print(StockBuyAndSell(arr))