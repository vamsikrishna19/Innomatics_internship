M,A=(int(input()),input().split())
N,B=(int(input()),input().split())
a=set(A)
b=set(B)
p=b.difference(a)
q=a.difference(b)
r=p.union(q)
print ('\n'.join(sorted(r, key=int)))
