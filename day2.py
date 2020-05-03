#square root and nth root
#prime numbers
#factorial 
#fibonocy
#gcd and lcm
#amstrong number
#palindrom and with slicing
#string reverse


  #square root
# from math import sqrt
# a=int(input())
# print(int(sqrt(a)))
# print(a**(1//5))


# #prime num
# n=int(input())
# l=[]
# for i in range(2,n):
#     flag=0
#     for j in range(2,i):
#         if(i%j==0):
#             flag=1
#             break
#     if(flag==0):
#         l.append(i)        
# print(*l)        

# n=int(input())
# def prime(n):
#     flag=0
#     for i in range(2,n):
#         if(n%i==0):
#             flag=1
#             break
    
#     return flag
# if(prime(n)==0):
#     print("prime")



# n=int(input())
# if(n<0):
#     print("Enter positive numbe")
# def fact(n):
#     if(n==1 or n==0):
#         return 1
#     else:
#         return n*fact(n-1)
# k=fact(n)
# print(k)


# n=int(input())
# count=1
# for i in range(n,0,-1):
#     count=count*i
# print(count)


# n=int(input())
# a=0
# b=1
# c=0
# l=[]
# print(a,b,end=" ")
# for i in range(n-2):
#     c=a+b
#     a=b
#     b=c
#     l.append(c)
# print(*l)

    
# n=int(input())
# a=int(input())
# b=int(input())
# def fib(a,b,n):
#     l=[]
    
# n=int(input())
# s=len(str(n))
# count=0
# for i in range(s):
#     k=(n%10)**s
#     n=n//10
#     count=count+k
 
# from math import gcd
# a=int(input())
# b=int(input())
# print(gcd(a,b))
# print((a*b)//gcd(a,b))


# a=int(input())
# b=int(input())
# def gcd(a,b):
#     while(b):
#         a,b=b,a%b

#     return a
# print(gcd(a,b))    


# s=input()
# s=s[::-1]
# print(s)


# s="hi this is hemanth"
# k=s.join("-")
# print(k)


a="python"
b=a.split("y")
print(a)