def main():

    print(discount([10, 4, 20]))  
 
    

def discount(item_prices):


    if type(item_prices) == list:
        for price in item_prices:
            if price <0:
                item_prices.remove(price)

# this function that returns the discount earned for a list of item prices.
    else:
        return None

# If a customer has ordered more than three items, the cheapest item is free.

    if len(item_prices) >= 3:
        item_prices.sort()
        return item_prices[0]

# if this function is called with a list of [10, 4, 20] then return 4.
# Return lowest price.
    else:
        return None

if __name__ == '__main__':
    main()

# Expect this to print 4