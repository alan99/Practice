MAX = float('inf')	# infinite number
print(MAX)
print(1000+MAX)

amount = 100
dp = [0] + [MAX] * amount
print(dp)

print([dp[amount], -1][dp[amount] == MAX])
print([dp[amount], -1][dp[amount] == 'x'])