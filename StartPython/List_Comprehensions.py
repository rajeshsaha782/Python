#Problem link -> https://www.hackerrank.com/challenges/list-comprehensions/problem

x = int(input())
y = int(input())
z = int(input())
n = int(input())
array = []
position = 0
for i in range ( x + 1 ) :
    for j in range( y + 1):
        for k in range(z + 1):
            if i+j+k != n:
                array.append([])
                array[position] = [ i , j ,k]
                position+=1

print (array)