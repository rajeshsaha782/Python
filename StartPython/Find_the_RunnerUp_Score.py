#Problem link -> https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
# from pip._vendor.distlib.compat import raw_input
#
# n=int(input())
# numbers=list(map(int,raw_input().strip().split()))[:n]
# maximum = max(numbers)
# numbers.remove(maximum)
# secondMaximum = max(numbers)
# print(secondMaximum)


#Problem link -> https://www.hackerrank.com/challenges/nested-list/problem
lowest=[]
secondLowest=[]
for _ in range(int(input())):
    name=input()
    score=float(input())
    if len(lowest)==0:
        #initialize lowest list
        lowest=[ [name,score] ]
    elif score < lowest[0][1]:
        secondLowest=lowest
        lowest=[ [name,score] ]
    elif score == lowest[0][1]:
        lowest.append( [name,score] )
    elif len(secondLowest)==0:
        secondLowest=[ [name,score] ]
    elif score < secondLowest[0][1]:
        secondLowest=[ [name,score] ]
    elif score == secondLowest[0][1]:
        secondLowest.append( [name,score] )
names=[item[0] for item in secondLowest]
for name in sorted(names):
    print(name)
