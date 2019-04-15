# Create a new dictionary  
d = dict() # or d = {} 
  
# Add a key - value pairs to dictionary 
d['xyz'] = 123
d['abc'] = 345
  
# print the whole dictionary 
print(d)
print(d.items())
print()

# print only the keys 
print(d.keys())
print()
  
# print only values 
print(d.values())
print()

# iterate over dictionary  
for i in d : 
    print("%s  %d" %(i, d[i]))
print()

# another method of iteration 
for index, key in enumerate(d): 
    print(index, key, d[key])
print()

# check if key exist 
print('xyz' in d)
  
# delete the key-value pair 
del d['xyz'] 
  
# check again  
print("xyz" in d)