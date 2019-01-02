#Problem link -> https://www.hackerrank.com/challenges/py-if-else/problem

n = int(input())
if n % 2 != 0:
    print("Weird")
else:
    if n in range(2, 5):
        print("Not Weird")
    elif n in range(6, 20):
        print("Weird")
    elif n > 20 and n<=100:
        print("Not Weird")
    else:
        print("Weird")