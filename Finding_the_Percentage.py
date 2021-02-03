from decimal import Decimal
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
query_score = student_marks[query_name]
total_score = sum(query_score)
avg = Decimal(total_score/3)
print(round(avg,2))
