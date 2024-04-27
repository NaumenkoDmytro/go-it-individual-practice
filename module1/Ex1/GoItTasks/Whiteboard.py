def count_ways(coins, amount):
    cache = {}
    def recursive_count(current_amount):
        if current_amount in cache:
            return cache[current_amount]
        elif current_amount == 0:
            return 1
        elif current_amount < 0:
            return 0 
    
        result = 0
        for coin in coins:
            result += recursive_count(current_amount - coin)

        cache[current_amount] = result
        return result
    return recursive_count(amount)
    
coins = [1, 3, 4]
amount = 10
print(count_ways(coins, amount))

