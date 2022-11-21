s1=input()

s2=input()
k=len(s2)-1
r=0
for i in  s1:
    if i==s2[k]:
        r+=1
print(r)
