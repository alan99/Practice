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
