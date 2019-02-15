# https://www.journaldev.com/19103/python-collections

from collections import Counter

marks_list = [
    ('Shubham', 89),
    ('Pankaj', 92),
    ('JournalDev', 99),
    ('JournalDev', 98)
]

count = Counter(name for name, marks in marks_list)
print(count)

print(list(count.values()))

print(list(count.elements()))

print(count.most_common(1))

c = Counter(['x', 'x', 'x', 'y', 'z', 'z'])
print(c.most_common(1))

print(c.values())
print(list(c.values()))

cc = dict(c.most_common(2))
print(cc.items())
print(cc.keys())
print(cc.values())


counts = Counter([(1, "A"), (2, "A"), (1, "A"), (2, "B"), (1, "B")])

cc = Counter({(f1, f2): n for (f1, f2), n in counts.items() if f2 == "A"}).most_common(2)
print(cc)

s = '123.345..0234'
print(s.split('.'))

ns = s.split('.')
print(int(ns[-1]))