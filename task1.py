import time
#Жадібні алгоритми
def find_coins_greedy(amount):
    coins = [50, 25, 10, 5, 2, 1]
    result = {}
    
    for coin in coins:
        if amount >= coin:
            num_coins = amount // coin
            result[coin] = num_coins
            amount -= coin * num_coins
    
    return result

# Приклад використання
amount = 113
print(find_coins_greedy(amount))

start_time = time.time()
greedy_result = find_coins_greedy(amount)
greedy_time = time.time() - start_time

print("Жадібний алгоритм результат:", greedy_result)
print("Час виконання жадібного алгоритму: {:.6f} секунд".format(greedy_time))
