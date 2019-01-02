#Problem link -> https://www.hackerrank.com/challenges/python-lists/problem

n = int(input())
list=[]
for _ in range(n):
    cmd, *value = input().split()
    if cmd=="insert":
        list.insert(int(value[0]),int(value[1]))
    elif cmd == "print":
        print(list)
    elif cmd == "remove":
        list.remove(int(value[0]))
    elif cmd == "append":
        list.append(int(value[0]))
    elif cmd == "sort":
        list.sort()
    elif cmd == "pop":
        list.pop()
    elif cmd == "reverse":
        list.reverse()


