n=int(input())
A=set(map(int, input().split()))
m=int(input())
B=set(map(int, input().split()))
C=A.intersection(B)
print(len(C))