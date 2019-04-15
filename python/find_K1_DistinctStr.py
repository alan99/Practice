from collections import defaultdict

def find_K1_DistinctStr(str, K):
	ans = []
	if K <= 1 or K > len(str):
		return ans

	dictStr = defaultdict(int)
	for c in str[:K]:
		dictStr[c] += 1

	if len(dictStr) == K-1:
		ans.append(str[:K])

	for i,c in enumerate(str[K:], K):
		dictStr[str[i-K]] -= 1
		dictStr[c] += 1
		if dictStr[str[i-K]] == 0:
			del dictStr[str[i-K]]

		if len(dictStr) == K-1:
			ans.append(str[i-K+1:i+1])

	return ans


print(find_K1_DistinctStr("aabcdefdfdc", 4))









