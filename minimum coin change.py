def min_coin_change(coins, amount):
    MAX = float('inf')
    dp = [MAX] * (amount + 1)
    dp[0] = 0
    for coin in coins:
        for x in range(coin, amount + 1):
            if dp[x - coin] != MAX:
                dp[x] = min(dp[x], dp[x - coin] + 1)
    return dp[amount if dp[amount] != MAX else - 1]

if __name__ == "__main__":
    coins = [1, 2, 5]
    amount = 11
    print("Minimum coins required:", min_coin_change(coins, amount))