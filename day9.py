# from math import sqrt
# a=int(input())
# k=intinput(*(input())
# print(sqrt(a))
# print(a**(1//k))


# a=int(input())
# l=[]
# for i in range(2,a):
#     flag=0
#     for j in range(2,i):
#         if(i%j==0):
#             flag=1
#             break
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
#         return 1
#     else:
#         return n*fact(n-1)
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
# l=[]
# for i in range(1,a):
#     if(a%i==0):
#         l.append(i)
# if(sum(l)==a):
#     print("perfect number")    

# a=int(input())
# def fib(n):
#     if(n==0 or n==1):
#         return n
#     else:
#         return(fib(n-1)+fib(n-2))
# for i in range(a):
#     print(fib(i),end=" ")    

# a=int(input())
# l=len(str(a))
# count=0
# for i in range(l):
#     c=(a%10)**l
#     count=count+c
#     a=a//10
# print(count)    
    
# from math import gcd
# a=10;b=20
# print(gcd(a,b)) 
# print((a*b)//gcd(a,b))   

# a=int(input())
# a=str(a)
# k=a[::-1]
# print(k)

# l=input()
# for i in range(len(l)):
#     s=l[::-1]
# print(s)    

# a=input()
# s=""
# for i in a:
#     if i not in s:
#         s=s+i
# print(s)        


# a=input()
# s=[[]]
# for i in range(len(a)):
#     for j in range(i+1,len(a)+1):
#         s.append(a[i:j])
# print(s)        

# l=["var","taru","tarun"]

# def fun(s):
#       return s[-1]

# l.sort(key=fun)  
# print(l)          


# l=[1,2,3,4]
# k=[7,8,9]
# o=[]
# m=min(len(l),len(k))
# for i in range(m):
#     o.append(l.pop(0))
#     o.append(k.pop(0))
# print(o+l+k)    


    