#square root and nth root
#prime numbers
#factorial 
#fibonocy
#gcd and lcm
#amstrong number
#palindrom and with slicing
#string reverse
#removing duplicates from list and string
#substrings
#sortings and types
#list coping ----------> l1=l[:]
#zip function
#iterotor --- next()
#matrix(list of lists) --- adding marix and multiplication matrix , rotating matrix , transpose a matrix    
# rotationg a string -- left rotation and rigt rotation 
#dictionaries --intialization and updating and reading
#combinint two list with alternative elements
#














              #------------------square and roots------------#
# import math
# n=8
# k=int(input())
# print(int(math.sqrt(n)))
# print(math.ceil(n**(1/k)))

            #----------------prime numbers-----------
# n=int(input())
# l=[]
# for i in range(2,n):
#     flag=0
#     for j in range(2,i):
#         if(i%j==0):
#             flag=1
            #  break
#     if(flag==0):
#         l.append(i)
# print(l)        



#       prime num for a digit

# n=int(input())
# Flag=0
# for i in range(2,n):
#     if(n%i==0):
#         Flag=1
# if(Flag==0):
#     print("It is prime")        



             #factorial
# n=int(input())
# for i in range(n-1,0,-1):
#     n=n*i
# print(n)   


         #-------------factorial using recursion--------------

# n=int(input())

# def factor(n):
#     if(n==1 or n==0):
#         return 1
#     else:
#         return n*factor(n-1)

# k=factor(n)
# print(k)        
                     
    
          #---------------------fibonocy series-------
# n=int(input())
# a=0
# b=1
#print(a,b,end=" ")
# c=0
# l=[]
# for i in range(n-2):
#     c=a+b
#     a=b
#     b=c
#     l.append(c)
# print(*l)


         #------------------fibonocy using reursion----------------

# n=int(input())
# def fib(n):
#     if(n<=1):
#         return n
#     else:
#         return(fib(n-1)+fib(n-2))

# if(n<0):
#     print("Enter positive integers") 
# else:
#     for i in range(10):
#         print(fib(i))       



      #-------------------amstrong number-------------------
# n=int(input())
# k=len(str(n))
# count=0
# for i in range(k):
#     m=(n%10)**k
#     n=n//10
#     count=count+m
# if(count==n):
#     print("it is an amstrong number")
# else:
#     print("not an amstron")    
                
                #--------------------matrix-------------------
# l=[6,5,76,8,3,2,2,4,5]
# sub=[]
# for i in range(0,len(l),3):
#     sub.append(l[i:i+3])
# print(sub)    
    
      #------------GCD and LCM----------

# from math import gcd
# a=int(input())
# b=int(input())
# print((a*b)//gcd(a,b))


  #----------GCD and LCM for a list and without inbuilt function--------

# from functools import reduce

# a=int(input())  

# b=int(input())

# l=[10,20,30]

# def gcdd(a,b):
#       while(b):
#             a,b=b,a%b
#       return a

# def lcmm(a,b):
#       return (a*b)//gcdd(a,b)

# print(gcdd(a,b))
# print(lcmm(a,b)) 

# print(reduce(gcdd,l))



#----------- remove duplicates in a list--------------

# l=[1,1,3,5,6,6,7,8,7]

# # print(set(l))

# a=[]
# for i in l:
#       if i not in a:
#             a.append(i)
# print(*a)            


# s="aaabbccddxyx"
# an=""
# for i in s:
#       if i not in an:
#             an=an+i
# print(an)


#-----------------------substrings----------------------

# l=list(input())
# sub=[[]]
# for i in range(len(l)):
#       for j in range(i+1,len(l)+1):
#             sub.append(l[i:j])
# print(sub)
# print()

#-------------------substrings for perticular lengths-----------










#sorting a list

# l=[7,3,9,2,1,5]
# k=l[:]
# l.sort()
# print(l)
# print(sorted(k))



#list coping

# l=[7,3,9,2,1,5]
# k=l[:]
# print(k)

#--------------------sorting types
 
    #using sort
# s=[2,9,5,8,1,4]
# s.sort()
# print(s)
 
     #using sorted()
# s=[2,9,5,8,1,4]
# k=sorted(s)
# print(k)


     #-------------- reverse sorting
# s=[2,9,5,8,1,4]
# s.sort(reverse=True)
# k=sorted(s,reverse=True)
# print(s,k)


      #--------------reversing based on last letter in the strings in a list using key
# l=["var","taru","tarun"]

# def fun(s):
#       return s[-1]

# l.sort(key=fun)  
# print(l)          



# l=["a","bbbbb","cc"]
# l.sort(reverse=True,key=len)
# print(l)

 
     #---------------using keys
# s=["aa","bf","g","gd","srf","mm"] 
# s.sort(key=len)
# print(s)

#--------------combining two list with alternative elements
# l=[2,3,4,7,9,10]
# m=["a","b","c"]
# k=[]
# n=min(len(l),len(m))
# for i in range(n):
#       k.append(l.pop(0))
#       k.append(m.pop(0))
# print(k+l+m)      


#-----------adding elemnts to a set
# n=int(input())
# l=set()
# for i in range(n):
#       b=input().split()
#       l.update(b)
# print(l)      




