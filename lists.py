list1 = list()
print(list1) # empty list

list2 = list([1,2,3])
print(list2) # [1, 2, 3]

list3 = list(["red", "blue", "green"])
print(list3) # ['red', 'blue', 'green']

list = []
print(list) # empty list

list = [1,2,3]
print(list) # [1, 2, 3]

list = ["green", "red", "blue"]
print(list) # ['green', 'red', 'blue']

import random 
list1 = [2, 4, 6, 33, 78, 22]
random.shuffle(list1)
print(list1) # shuffled list1

combineList = list2 + list3
print(combineList) # [1, 2, 3, 'red', 'blue', 'green']

lengthOfList1 = len(list1)
print(lengthOfList1) # length of list1

print(list1)

print(list1[1]) # second element of list1
print(list1[1:3]) # elements from index 1 to 2 of list1
print(list1[-1:-4:-1]) # last three elements of list1 in reverse order
print(list1[:4]) # first four elements of list1
print(list1[2:]) # elements from index 2 to end of list1
print(list1[:-2]) # all elements of list1 except last two
print(list1[:]) # all elements of list1
print(list1[::-1]) # all elements of list1 in reverse order

# List Methods 
newlist = list1.copy()
print(newlist) # copy of list1
newlist.append(99)
print(newlist) # newlist after appending 99
newlist.insert(2, 22)
print(newlist) # newlist after inserting 22 at index 2
newlist.insert(4, 44)
print(newlist) # newlist after inserting 44 at index 4
newlist.remove(22)
print(newlist) # newlist after removing first occurrence of 22
newlist.pop()
print(newlist) # newlist after removing last element
newlist.reverse()
print(newlist) # newlist after reversing
newlist.sort()
print(newlist) # newlist after sorting in ascending order
newlist.sort(reverse=True)
print(newlist) #descending order
newlist.clear()
print(newlist)
del newlist # delete the list compleletly means you have to define again

def main():
    x = 1
    y = [1,2,3,4]
    m(x,y)
    print("x is ", x)
    print("y[0] is ", y[0])

def m(number, numbers):
    number = 5555
    numbers[0] = 22
main()
    
 
listx = [2,3,5,7,8]
def reverse(listx):
    reversedList = []
    for i in listx:
        reversedList.insert(0, i)
    return reversedList
print(reverse(listx))
# THAT ABOVE ONE WAS FKING HARD THO 

def add(x, listx=[]):
    listx.append(x)
    return listx

add(1)
add(4)
print(add(5))

list1 = ["Hasnain", "Ali", "Hassan"]
print(list1.count("Ali"))

list2 = ["Hasnain", "Ali", "Hassan", "Ali"]
print(list2.index("Hasnain"))