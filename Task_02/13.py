n = int(input())
s = set(map(int,input().split()))
m = int(input())
r = set(map(int,input().split()))
print(len(s.intersection(r)))