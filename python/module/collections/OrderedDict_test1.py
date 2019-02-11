colours =  {"Red" : 198, "Green" : 170, "Blue" : 160}
for key, value in colours.items():
    print(key, value)
# Output:
#   Green 170
#   Blue 160
#   Red 198
# Entries are retrieved in an unpredictable order

##########################################

from collections import OrderedDict

colours = OrderedDict([("Red", 198), ("Green", 170), ("Blue", 160)])
for key, value in colours.items():
    print(key, value)
# Output:
#   Red 198
#   Green 170
#   Blue 160
# Insertion order is preserved

print(dict(colours)['Red'])

