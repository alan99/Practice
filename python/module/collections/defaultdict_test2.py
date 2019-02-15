from collections import defaultdict
s = 'mississippi'
d = defaultdict(int)
for k in s:
	d[k] += 1
print(d)
print(dict(d))



ice_cream = defaultdict(lambda: 'Vanilla')

ice_cream['Sarah'] = 'Chunky Monkey'
ice_cream['Abdul'] = 'Butter Pecan'

print(ice_cream['Sarah'])
print(ice_cream['Joe'])