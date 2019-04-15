# closest two sum < target, return pair

def twoSum(nums, target):
	nums.sort()
	l, r = 0, len(nums)-1
	d = float('inf')
	res = [float('-inf')]*2

	while l < r:
		cur = nums[l] + nums[r]
		diff = target - cur

		if diff < d and diff >= 0:
			d = diff
			res = [nums[l], nums[r]]

		if cur  < target:
			l += 1
		else:
			r -= 1

	return res

L = [2,1,2,2,2,1,1,4,5]
print(twoSum(L,12))