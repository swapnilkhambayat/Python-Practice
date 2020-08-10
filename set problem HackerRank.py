m = int(input())
mv = set(input().split())
n = int(input())
nv =  set(input().split())
sd = mv.symmetric_difference(nv)

print('\n'.join(sorted(mv.difference(nv).union(nv.difference(mv)), key=int)))
