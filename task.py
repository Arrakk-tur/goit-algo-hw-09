import time


def find_coins_greedy(amount):
    denominations = [50, 20, 10, 5, 2, 1]
    result = {}

    for coin in denominations:
        if amount >= coin:
            count = amount // coin
            amount -= count * coin
            result[coin] = count

    return result


def find_min_coins(amount):
    denominations = [1, 2, 5, 10, 20, 50]
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    coin_used = [-1] * (amount + 1)

    for coin in denominations:
        for i in range(coin, amount + 1):
            if dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                coin_used[i] = coin

    result = {}
    while amount > 0:
        coin = coin_used[amount]
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        amount -= coin

    return result


# Вимірювання часу виконання
amount = 95638

start_time = time.time()
greedy_result = find_coins_greedy(amount)
greedy_time = time.time() - start_time

start_time = time.time()
dp_result = find_min_coins(amount)
dp_time = time.time() - start_time

print("Greedy approach result:", greedy_result)
print("Greedy approach time: {:.6f} seconds".format(greedy_time))

print("Dynamic programming approach result:", dp_result)
print("Dynamic programming approach time: {:.6f} seconds".format(dp_time))
