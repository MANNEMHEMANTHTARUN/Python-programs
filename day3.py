    #1
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
#             break
#     if(flag==0):
#         l.append(i) 
# print(*l)        


      #2
# n=int(input())
# count=1
# for i in range(n,0,-1):
#     count=count*i
# print(count)    
      
#3
# n=int(input())
# if(n<0):
#     print("Enter positive numbers")
# def fact(n):
#     if(n==0 or n==1):
#         return 1
#     else:
#         return n*(fact(n-1))
            
# print(fact(n))    


#4
# n=int(input())
# a=0
# b=1
# l=[]
# print(a,b,end=" ")
# for i in range(n-2):
#     c=a+b 
#     a=b
#     b=c
#     l.append(c)
# print(*l)


#5
# n=int(input())
# def fib(n):
#     if(n<2):
#         return(1)
#     else:
#         return(fib(n-1)+fib(n-2))
# for i in range(n):
#     print(fib(i))

# from math import gcd
# a=int(input())
# b=int(input())
# print(gcd(a,b))


# a=int(input())
# b=int(input())
# while(b):
#     a,b=b,a%b
# print(a)    


# from functools import reduce
# l=list(map(int,input().split()))
# def gcdd(a,b):
#     while(b):
#         a,b=b,a%b
#     return a 
# print(reduce(gcdd,l))



