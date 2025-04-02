
def maxProfit(prices):
    min_price = float('inf') 
    max_profit = 0  

    for price in prices:
        if price < min_price:
            min_price = price  # Price update
        elif price - min_price > max_profit:
            max_profit = price - min_price  # Profit update

    return max_profit

def maxProfitB(prices):
    cur_min = prices[0]
    cur_max = prices[0]
    cur_ans = 0

    for p in prices:
        if p > cur_max:
            cur_max = p
            cur_ans = max(cur_ans, cur_max - cur_min)
        
        elif p < cur_min:
            cur_min = p
            cur_max = p
    return cur_ans


if __name__ == '__main__':

    prices = [7,1,5,3,6,4]  #expected return 5
    


    print("Número de elementos restantes:", maxProfit(prices))

    print("Número de elementos restantes:", maxProfitB(prices))


# 121. Best Time to Buy and Sell Stock