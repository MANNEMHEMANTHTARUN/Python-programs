# from math import sqrt
# a=int(input())
# k=int(input())
<<<<<<< HEAD
# print(sqrt(a))
# print(a**(1//k))

# a=int(input())
#   if(i%j==0):
#             flag=1
#             break
#     if(flag==0):
#             l.append(i)
# print(*l)    l=[]
# for i in range(2,a):
#     flag=0
#     for j in range(2,i):


# a=int(input())
# k=len(str(a))
# count=0
# for i in range(k):
#     c=(a%10)**k
#     count=count+c
#     a=a//10
# print(count)    

# from math import gcd    
# a=int(input())
# b=int(input())
# while(b):
#     a,b=b,a//b
# print(gcd(a,b))

# a=int(input())
# k=[]
# for i in range(a):
#     l=list(map(int,input().split()))
#     k.append(l)
# print(k) 
# m=list(zip(*k)) 
# for i in range(len(m)):
#     m[i]=list(m[i])
# print(m)    


# a=int(input())
# for i in range(a):
#     for j in range(a-i+1):
#         print(" ",end="")
#     for j in range(i+1):
#         print("*",end="")    
#     print()    

# a=int(input())
# sp=a-1
# st=1
# for i in range(a):
#     print(" "*sp,end="")
#     sp=sp-1
#     print("*"*st,end="")
#     st=st+1    
#     print()



# a=int(input())
# f=a
# s=0
# f1=a
# for i in range(a+1):
    
#     for j in range(f+1):
#         if(j==f):
#             print(j,end=" ")
#         else:
#             print(j,end=" ")
#     f=f-1
    
#     if(i!=0):
#         print(" "*s,end="")
#     s=s+4
    
#     for j in range(f1,-1,-1):
#         if(j==0):
#             print(j,end="")
#         else:
#             print(j,end=" ")
            
#     f1=f1-1
    
#     print()   
    
# for i in range(ord("a"),ord("z")+1):
#     print(chr(i),end=" ")  


# a=int(input())
# for i in range(a):
#     m=1
#     for k in range(i):
#         print(" ",end="")
#     for j in range(a,i,-1):
#         print(m,end="")
#         m=m+1
#     print()    


# l=list(map(int,input().split()))
# s=[]
# for i in l:
#     if i not in s:
#         s.append(i)
# print(s)        
=======
# print("square root of a is {}".format(sqrt(a)))


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
# print(l)        



# l=list(map(int,input().split()))
# k=[]
# for i in l:
#     flag=0
#     for j in range(2,i):
#         if(i%j==0):
#             flag=1
#             break
#     if(flag==0):
#         k.append(i)
# print(k)            


# n=int(input())
# k=[]
# for i in range(1,n):
#     if(n%i==0):
#         k.append(i)
# print(sum(k))        


# n=int(input())
# a=0
# b=1
# print(a,b,end=" ")
# for i in range(n-2):
#     c=a+b
#     a=b
#     b=c
#     print(c,end=" ")

    



# n=int(input())
# count=1
# for i in range(n,1,-1):
#     count=count*i
# print(count)


# n=int(input())
# def fact(n):
#     if(n<2):
#         return 1
#     else:
#         return n*fact(n-1)
# print(fact(n))           


# a=int(input())
# if(a%4==0):
#     if(a%100==0):
#         if(a%400==0):
#             print("leap year")
#         else:
#             print("not a leap year")
#     else:
#         print("leap year")
# else:
#     print("not a leap year")                    


# from math import gcd
# a,b=int(input()),int(input())
# k=gcd(a,b)
# lcm=a*b//k
# print(lcm)


# a=int(input())
# b=int(input())
# while(b):
#     a,b=b,a%b
# print(a)


# a=int(input())
# k=len(str(a))
# c=0
# for i in range(k):
#     m=a%10
#     c=c+m**k
#     a=a//10
# print(c)    

# m=int(input())
# l=[]
# for i in range(m):
#     s=list(map(int,input().split()))
#     l.append(s)
# print(l)


# l=[1,2,3,4,5,6,7,8,9]
# k=int(input())
# s=[]
# for i in range(0,len(l),k):
#     s.append(l[i:i+k])
# s1=list(zip(*s))
# for i in range(len(s1)):
#     s1[i]=list(s1[i])
# print(s1)    


l=[1,2,3,4,5]
k=[5,6,7,8,9]
m=min(len(l),len(k))
for i in range(m):
    
>>>>>>> 9569d3cfe40160b39c367a8642d08ef946b1ffd4
