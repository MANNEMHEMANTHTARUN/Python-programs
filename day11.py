# from math import sqrt
# a=int(input())
# k=int(input())
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