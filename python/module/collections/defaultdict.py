from collections import defaultdict

marks = [
    ('Shubham', 89),
    ('Pankaj', 92),
    ('JournalDev', 99),
    ('JournalDev', 98)
]

dict_marks = defaultdict(list)

for key, value in marks:
    dict_marks[key].append(value)

print(list(dict_marks.items()))