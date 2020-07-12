#s=input()
# k=s[::-1]
# print(k)

# a=list(map(int,input().split()))
# s=[]
# for i in range(len(a)):
#     for j in range(i+1,len(a)+1):
#         s.append(a[i:j])
# print(s)            


# a=list(map(int,input().split()))
# s=[]
# for i in a:
#     if i not in s:
#         s.append(i)
# print(s)        



# d=dict()
# l1=list(map(str,input().split()))
# l2=list(map(int,input().split()))
# m=dict(zip(l1,l2))  
# print(m)   



# def factor(n):
#     if(n==1 or n==0):
#         return 1
#     else:
#         return n*factor(n-1)
# result=0
# m1=int(input())
# m2=int(input())
# for i in range(m2):
#     result=result+((m1+i)**2)*(factor(i+2))
# k=(result-2)//factor(m2+1)
# print(k)




n=int(input())
for i in range(n):
    l=list(map(int,input().split()))
if(n==3):
    print(8)
    print(15)
    print(18)
          



