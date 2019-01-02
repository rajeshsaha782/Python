#Problem link -> https://www.hackerrank.com/challenges/finding-the-percentage/problem

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    total=0
    avg=0
    for i in range(3):
        total+=student_marks[query_name][i]
    avg=total/3
    print(avg)

