<<<<<<< HEAD
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


# a=int(input())
# count=1
# for i in range(a,0,-1):
#     count=count*i
# print(count)


# n=int(input())
# def fact(n):
#     if(n<2):
#         return 1
#     else:
#         return n*fact(n-1)
# print(fbact(n))


# n=int(input())
# a=0
# b=1
# print(a,b,end=" ")
# l=[]
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


# l=[1,2,3,4]
# m=["a","b","c"]
# n=[]
# k=min(len(l),len(m))
# for i in range(k):
#     n.append(l.pop())
#     n.append(m.pop())
# print(n+l+m)


# l={1,2,3,4}
# m={"a","b"}
# print(l.update(m))

l={1,2,3,4}
m=[4,5,6]
m=set(map(int,m))
print(l^m)
=======
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


# a=int(input())
# count=1
# for i in range(a,0,-1):
#     count=count*i
# print(count)


# n=int(input())
# def fact(n):
#     if(n<2):
#         return 1
#     else:
#         return n*fact(n-1)
# print(fbact(n))


# n=int(input())
# a=0
# b=1
# print(a,b,end=" ")
# l=[]
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


# l=[1,2,3,4]
# m=["a","b","c"]
# n=[]
# k=min(len(l),len(m))
# for i in range(k):
#     n.append(l.pop())
#     n.append(m.pop())
# print(n+l+m)


# l={1,2,3,4}
# m={"a","b"}
# print(l.update(m))

l={1,2,3,4}
m=[4,5,6]
m=set(map(int,m))
print(l^m)
>>>>>>> d6799ee5a72f4264da179ba8c736a1f1115211c4
