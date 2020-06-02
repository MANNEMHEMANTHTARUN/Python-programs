                                        # Inbult functions
            #list in bult functions
      #append()	Adds an element at the end of the list
      # clear()	Removes all the elements from the list
      # copy()	Returns a copy of the list
      # count()	Returns the number of elements with the specified value
      # extend()	Add the elements of a list (or any iterable), to the end of the current list
      # index()	Returns the index of the first element with the specified value
      # insert()	Adds an element at the specified position
      # pop()	Removes the element at the specified position
      # remove()	Removes the first item with the specified value
      # reverse()	Reverses the order of the list
      # sort()	Sorts the list



#----------list functions-------------------#
# a=[2,8,5,9]
# a.append(7)
# print(a)
# a.sort(reverse=True)
# print(a)
# a.reverse()
# print(a)
# print(a.count(2))
# k=a.copy()
# print(k)
# k=[]  
# print(a.index(2))
# k.extend(a)
# print(k)


#----------------------set function---------#
s={1,2,3,4,3,3,4,5,5}
s.add(5)
print(s)
s.clear()
print(s)
k=s.copy()
print(k)
k={2,8,9,0,3,4,5}
print(s.difference(k))
