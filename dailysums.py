#square root and nth root
#types of reading
#prime numbers
#factorial 
#fibonocy
#gcd and lcm
#amstrong number
#palindrom and with slicing
#string reverse
#removing duplicates from list and string
#substrings
#perutations and combinations
#sortings and types
#list coping ----------> l1=l[:]
#iterotor --- next()
#matrix(list of lists) --- adding marix and multiplication matrix , rotating matrix , transpose a matrix    
# rotationg a string -- left rotation and rigt rotation 
#dictionaries --intialization and updating and reading
#combinint two list with alternative elements
<<<<<<< HEAD
#join(joiniing a list to string) and split

#finding the number of occurence of a substring in a given string

#zip function and "*"-->lists and tuples unpacking and sets ,and "**"-->for dictionaries unpacking

#leap year


=======
#any and all functons 
#pattern sums
#----leap year----
>>>>>>> 9569d3cfe40160b39c367a8642d08ef946b1ffd4














              #------------------square and roots------------#
# import math
# n=8
# k=int(input())
# print(int(math.sqrt(n)))
# print(math.ceil(n**(1/k)))

#------typers of  reading inputs
a=int(input())
a,b=input().split()
a,*b=input().split()
print(a,b)

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
<<<<<<< HEAD


           #------------------matrix multiplication-----------
           
# import numpy as np 
# b=np.array([[2,10,20],[80,43,31],[22,43,10]])
# print(b)
# print(np.amin(b,0))
# print(np.amax(b,0))
# print(np.amin(b,1))
# print(np.amax(b,1))           
           
           
               
=======
    
                  #-------------------matrix reading ---------
# s=int(input())

# m=[ list(map(int,input().split())) for i in range(s)]



# print(*m)




>>>>>>> 9569d3cfe40160b39c367a8642d08ef946b1ffd4
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

<<<<<<< HEAD
#-------------------substrings for perticular lengths-----------
# a=list(map(int,input().split()))
# k=int(input())
# l=[]
# for i in range(0,len(a),k):
#       s=a[i:i+k]
#       l.append(s)
# print(l)      
      
=======

# from itertools import permutations as p
# from itertools import combinations as c
# from itertools import combinations_with_replacement as cr

# # l=[1,5,6,8]
# # l=[1,6,-1,5,-2,7,2,10]
# # k=[]
# # # print(list(p(l)))
# # # print("combinations here")

# # for i in range(1,len(l)+1):
# #     m=list(c(l,i))
# #     k=k+m
    
# # k1=[x for x in k if sum(x)==6]    
# # print(k1)    
    
# #pritnting conminations with replacements

# s="abc"
# print(list(c(s,2)))
# print(list(cr(s,2)))

#-------------------substrings for perticular lengths-----------

# a=[1,2,3,4,5,6,7,8]
# k=[]
# for i in range(len(a)):
#       for j in range(i+1,len(a)+1):
#             m=a[i:j]
#             if(len(m)==3):
#                   k.append(m)
# print(k)

>>>>>>> 9569d3cfe40160b39c367a8642d08ef946b1ffd4







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

#--------------  join() and spilt() -----------opposite sitring funtions


# a="my name is hemanth"
# print("This is the list of string a",a.split(" "))
# b=["hi","this"]
# s="-"
# b=s.join(b)
# print(b)


# a=["happy"]*5
# a=a+["birth day","to","you"]

# # print(a)

# #------------------------ zip funtion ---------

# k=dict(zip([1,3,4],"abc"))
# # p=k.values()
# # print(*p)
# # print(k.keys())

# # print(k.items())
# # # print(*a,sep="-")


# for i,j in k.items():
#       print(i)
#       print(j)




#finding the number of occurence of a substring in a given string

# s = 'arunununghhjj'
# sb = 'nun'
# results = 0
# sub_len = len(sb)
# for i in range(len(s)):
#     if s[i:i+sub_len] == sb:
#         results += 1
# print results



#-------------------------sorting--------------------#


# d={}

# l=[1,2,4]
# s="cba"

# d=dict(zip(l,s))

# k=list(d.keys())
# v=list(d.values())

# for (k,v) in d.items():
#       if(k==2):
#             d[k]="s"
# print(d)            
            

# print(sorted(zip(s,k)))

#------all and any functions
# string =input()
# print(any(c.isalnum() for c in string))
# print(any(c.isalpha() for c in string))
# print(any(c.isdigit() for c in string))
# print(any(c.islower() for c in string))
# print(any(c.isupper() for c in string))


#------zip functions---
# l=[[1,2,3],[3,4,5],[7,8,9]]
# l2=list(zip(*l))
# print([ list(i) for i in l2])




# letters = ['b', 'a', 'd', 'c']
# numbers = [2, 4, 3, 1]
# data1 = list(zip(letters, numbers))
# data1
# [('b', 2), ('a', 4), ('d', 3), ('c', 1)]
# data1.sort()  # Sort by letters
# data1
# [('a', 4), ('b', 2), ('c', 1), ('d', 3)]
# data2 = list(zip(numbers, letters))
# data2
# [(2, 'b'), (4, 'a'), (3, 'd'), (1, 'c')]
# data2.sort()  # Sort by numbers
# data2
# [(1, 'c'), (2, 'b'), (3, 'd'), (4, 'a')]


#--pattern sums------#
# a=int(input())
# for i in range(a):
#       for j in range(i+1):
#             print(j,end="")
#       print()      


# a=int(input())
# for i in range(a):
#       for j in range(i+1):
#             print("*",end='')
#       print()      


# a=int(input())
# s=1
# m=1
# for i in range(1,a+1):
#       print(" "*(a-i),end="")
#       print("*"*i,end="")      
#       print()      

#--leap year---
# a=int(input())
# if(a%4==0):
#       if(a%100==0):
#             if(a%400==0):
#                   print("Leap year")
#             else:
#                   print("not a leap year")
#       else:
#             print("leap year")
# else:
#       print("not a leap year")                              



# n=int(input())
# k=1
# for i in range(n):
#       for j in range(1,i+2):
#             print(j,end="")
#             k=k+1
#       print()      



# n=int(input())
# l=[]
# for i in range(2,n):
#       flag=0
#       for j in range(2,i):
#             if(i%j==0):
#                   flag=1
#                   break
#       if(flag==0):
#             l.append(i)
# c=2
# for i in range(1,len(l)):
#       c=c+l[i]
#       if c in l:
#             print(c)



# n=int(input())
# for i in range(n):
#       for j in range(i+1):
#             m=0
#             print(j+m,end=" ")
#             if(j%2==0):
#                   m=m*2
#       print()
      
# n=int(input())
# print(1)
# for i in range(n):
#       for j in range(i+1,-1,-1):
#             print(2**j,end=" ")
#       print()      



n=int(input())
for i in range(n):
      for j in range(2**(i)):
            print("*",end="")
      print()      

<<<<<<< HEAD
# letters = ['b', 'a', 'd', 'c']
# numbers = [2, 4, 3, 1]
# data1 = list(zip(letters, numbers))
# data1
# [('b', 2), ('a', 4), ('d', 3), ('c', 1)]
# data1.sort()  # Sort by letters
# data1
# [('a', 4), ('b', 2), ('c', 1), ('d', 3)]
# data2 = list(zip(numbers, letters))
# data2
# [(2, 'b'), (4, 'a'), (3, 'd'), (1, 'c')]
# data2.sort()  # Sort by numbers
# data2
# [(1, 'c'), (2, 'b'), (3, 'd'), (4, 'a')]

#----leap year---- 
# a=int(input())
# if(a%4==0):
#       if(a%100==0):
#             if(a%400==0):
#                   print("leap year")
#             else:
#                   print("not a leap year")
#       else:
#             print("leap year")
# else:
#       print("not a leap year") 


# def hemu(l):
#       return " ".join(l[i] for i in range(0,len(l)))
# l=list(map(str,input().split()))
# print(hemu(l))
                                   




# for i in range(n):
#     k=input().split()
#     a=k[0]
#     b=k[1]
#     if(a=="add"):
#         l.append(b)    
#     elif(a=="find"):
#         count=0
#         for i in l:
#             if(b[0]==i[0]):
                
#                 if b in i:
#                     count=0
#                     count=count+1
# print(l)         




           
        
=======
>>>>>>> 9569d3cfe40160b39c367a8642d08ef946b1ffd4
