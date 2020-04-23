# l=[1,2,34,4]
# k=[8,9,90]
# p=[]
# m=min(len(l),len(k))
# for i in range(m):
#     p.append(l.pop(0))
#     p.append(k.pop(0))
# print(p+l+k)    
    
# s=set()
# for i in range(10):
#     s.add(i)
# print(s)        


# l=[1,2,3,4]
# s=""
# for i in range(len(l)):
#     s=s+str(i)
# print(s)    

# l="hi this is hemanth tarun"
# k=l.split()
# s=""
# s=s.join(k)
# print(s)


# s="hii"
# l=[]
# for i in range(len(s)):
#     for j in range(i+1,len(s)+1):
#         l.append(s[i:j])
# print(l)        
    
# s="kadsjhflrojorajsoisjvoprjaw"
# a="aeiou"
# k=""
# for i in s:
#     if i  in a:
#         k=k+i
# print(k)        
        

s="lslfhlfhlsfls" 
h="fhl"
k=[]   
for i in range(len(s)):
    for j in range(i+1,len(s)+1):
        k.append(s[i:j])
print(k)        