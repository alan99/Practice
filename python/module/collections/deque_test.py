
import collections
print("From the right")
d = collections.deque('abcdefg')
while True:
    try:
        print(d.pop())
    except IndexError:
        break
print()
 


print('\n From the left')
d = collections.deque(range(6))
while True:
    try:
        print(d.popleft())
    except IndexError:
        break
print()



d = collections.deque('abcdefg')
print('Deque:', d)
print('Length:', len(d))
print('Left end:', d[0])
print('Right end:', d[-1])
 
d.remove('c')
print('remove(c):', d)