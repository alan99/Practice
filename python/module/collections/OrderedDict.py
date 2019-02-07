# https://www.journaldev.com/19103/python-collections

from collections import OrderedDict

roll_no = OrderedDict([
    (11, 'Shubham'),
    (9, 'Pankaj'),
    (17, 'JournalDev'),
])

for key, value in roll_no.items():
    print(key, value)