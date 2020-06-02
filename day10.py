#---------square root------
# from math import sqrt
# s=int(input())
# k=int(input())
# print(sqrt(s))
# print(s**(1//k))

#---------prime numbers---
# a=int(input())
# l=[]
# for i in range(2,a):
#     count=0
#     for j in range(2,i):
#         if(i%j==0):
#             count=1
#             break
#     if(count==0):
#         l.append(i)
# print(*l)           

#-----------fibanoci series--
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


#---------with recurtion------
# n=int(input())
# def fib(n):
#     if(n==0 or n==1):
#         return(n)
#     else:
#         return (fib(n-1)+fib(n-2))
# for i in range(n):
#     print(fib(i))            


#---------factorial
# a=int(input())
# count=1
# for i in range(a,0,-1):
#     count=count*i
# print(count)


#------with recurtionn-
# a=int(input())
# def rec(a):
#     if(a<2):
#         return(1)
#     else:
#         return a*rec(a-1)
# print(rec(a))        

#-----amstrong
# a=int(input())
# k=len(str(a))
# count=0
# for i in range(k):
#     c=(a%10)**k
#     count=count+c
#     a=a//10
# print(count)    


#----------perfect number
# a=int(input())
# l=[]
# for i in range(1,a):
#     if(a%i==0):
#         l.append(i)
# print(sum(l))


#------gcd
# from math import gcd
# a=int(input())
# b=int(input())
# print(gcd(a,b))

# a=int(input())
# b=int(input())
# while(b):
#     a,b=b,a%b
#     print(a)


#------pallindrom
# a=input()
# b=a[::-1]
# if(a==b):
#     print("polindrome")
# else:
#     print("No")    

#---removing duplactes
# a=input()
# s=""
# for i in a:
#     if i not in s:
#         s=s+i
# print(s)         


# a=[1,2,3,4]
# k=len(a)
# s=[[]]
# for i in range(k):
#     for j in range(i+1,k+1):
#         s.append(a[i:j])
# print(*s)


# s=["amn","uodsf","udfisadf"]
# def us(s):
#     return s[-1]
# s.sort(reverse=True,key=us)
# print(s)     


# s=int(input())
# m=[list(map(int,input().split())) for i in range(s) ]
# k=[ m[i][i] for i in range(s)]
# n=[m[i][j] for i in range(s) for j in range(s) if(i+j+1==s)]
# print(sum(k)-sum(n))

#------transpose of matrx----
# l=[[1,2,3],[3,4,5],[7,8,9]]
# l2=list(zip(*l))
# print([ list(i) for i in l2])


