# from math import sqrt
# a=int(input())
# k=int(input())
# print(sqrt(a))
# print(a**(1//k))

# a=int(input())
# l=[]
# for i in range(2,a):
#     flag=0
#     for j in range(2,i):
#         if(i%j==0):
#             flag=1
#     if(flag==0):
#         l.append(i)
# print(*l)



# a=int(input())
# count=1
# for i in range(a,0,-1):
#     count=count*i
# print(count)



# a=int(input())
# def fact(n):
#     if(n<2):
#         return (1)
#     else:
#         return(n*fact(n-1))
# print(fact(a))            



# n=int(input())
# a=0
# b=1
# l=[]
# print(a,b,end=" ")
# for i in range(n-2):
#     c=a+b
#     l.append(c)
#     a=b
#     b=c
    
# print(*l)



# a=int(input())
# def fib(a):
#     if(a==0 or a==1):
#         return a
#     else:
#         return(fib(a-1)+fib(a-2))
# for i in range(a):
#     print(fib(i))



# a=int(input())
# b=len(str(a))
# count=0
# for i in range(b):
#     k=(a%10)**b
#     count=count+k
#     a=a//10
# print(count)    

 
# from math import gcd
# a=int(input())
# b=int(input())
# print(gcd(a,b))
# while(b):
#     a,b=b,a%b
#     print(a)


