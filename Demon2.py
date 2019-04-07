'''
i=1
sum=0
while i<=100:
    if i%2==0:
        sum=sum+i
    i=i+1;
print("之和为", sum)

i=1
while i<=100:
    if i%3==0 and i%5==0:
        print(i)
    i=i+1;
    '''
# #正方形
i=1
while i<=4:
     j=1
     while j <=4:
         print("*\t",end="")
         j+=1
     print()
     i=i+1;
# #直角三角形
# i=1
# while i<=4:
#     j=1
#     while j <=i:
#         print("*\t",end="")
#         j+=1
#     print()
#     i=i+1;
# #倒立直角三角形
#
# i=4
# while i>=1:
#     j=1
#     while j <=i:
#         print("*\t",end="")
#         j+=1
#     print()
#     i=i-1;
#
# #一三五直角三角形
# i=1
# while i<=4:
#     j=1
#     while j <=i*2-1:
#         print("*\t",end="")
#         j+=1
#     print()
#     i=i+1;
#菱形
i=1
while i<=4:
    a = 3
    while a>=i:
        print(" ", end="")
        a -= 1
    j=1
    while j<=2*i-1:
        print("*",end="")
        j+=1
    print()
    i+=1
b=1
while b<=3:
    c=1
    while c<=b:
        print(" ",end="")
        c+=1
    e=5
    while e>=2*b-1:
        print("*",end="")
        e-=1
    print()
    b+=1






