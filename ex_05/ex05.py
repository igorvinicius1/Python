x = int(input())
y = int(input())
s = 0

if x == y or x+1 == y-1 and x+1 % 2 == 0 or y+1 == x-1 and y+1 % 2 == 0:
    print('{}' .format(s))

if x < y:
    for i in (x+1, y-1):
        if(i % 2 != 0):
            s = s + i
            print('{}' .format(s))
            exit()
            
if x > y:
    for i in (y+1, x-1):
        if(i % 2 != 0):
            s = s + i
            print('{}' .format(s))
            exit()