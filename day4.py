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





# a=int(input())
# def fact(a):
#     if(a==0 or a==1):
#         return 1
#     else:
#         return a*fact(a-1)
# print(fact(a))            



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



# a=int(input())
# l=[]
# def fib(a):
#     if(a<2):
#         return a

#     else:
#         return(fib(a-1)+fib(a-2))
# for i in range(a):
#     l.append(fib(i))
# print(*l)    



l=[1,2,3,4]
l.sort(reverse=True)
print(l)



