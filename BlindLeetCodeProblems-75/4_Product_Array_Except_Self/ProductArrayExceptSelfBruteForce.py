arr = [10, 3, 5, 6, 2]

def ProductArrayExceptSelf(arr):
    product_array = []
    for i in range(len(arr)):
        product = 1
        for j in range(len(arr)):
            if i != j:
                product *= arr[j]
        product_array.append(product)
        
    return product_array
    
print(ProductArrayExceptSelf(arr))