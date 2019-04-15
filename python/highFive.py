import collections
import heapq
def highFive(arr):
	res = collections.defaultdict(list)

	for i, v in arr:
		if len(res[i]) < 5:
			heapq.heappush(res[i], v)
		else:
			heapq.heappushpop(res[i], v)

	ans = [[k, sum(res[k])/len(res[k])] for k in res.keys()]

	return ans

L = [[1,91],[1,92],[2,93],[2,99],[2,98],[2,97],[1,60],[1,58],[2,100],[1,61]]
print(highFive(L))