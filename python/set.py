s = set([1,1,2,3,3])
print(list(s))

s.add(4)
print(list(s))

s.add(4)
print(list(s))

s.remove(4)
print(list(s))




s1 = set([1,2,3])
s2 = set([2,3,4])

print(list(s1&s2))
print(list(s1|s2))

print(list(s1-s2))
print(list(s2-s1))

print(sum(s1))
print(sum(s2))

print(len(s1))