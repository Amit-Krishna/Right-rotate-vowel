a=input("a: ")
b="aeiouAEIOU"
d=1
c=""
for i in a:
    if i in b:
        c=a[-d]+c
        d=d+1
c=""+a[d:len(a)+1]
print(c)
