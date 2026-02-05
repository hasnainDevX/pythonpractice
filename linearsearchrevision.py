# str = "Hasnain"
# if 'a' in str:
#     print("Found a")
# list1 = [10, 20, 30, 40]
# if 50 not in list1:
#     print("50 not found")

# def linearSearch(arr, target):
#     for i in range(len(arr)):
#         if arr[i] == target:
#             return i
#     return -1
# print(linearSearch([1,2,3,4], 3))
# print(linearSearch(['a', 'b', 'c'], 'd'))
# print(linearSearch(["apple", "banana", "cherry"], "banana"))

# vowels = ['i', 'u', 'a', 'o', 'e']
# vowels.sort()
# print(vowels)

# x = [1,2,3,4,5]
# print(sorted(x))

# print("Reverse Sort")
# print(sorted(x, reverse=True))

# TUPLE 
tup1 = (1, 2, 3, 4, 5)
# print(tup1)
# print(max(tup1))
# print(min(tup1))
# print(sum(tup1))
# print(len(tup1))
# print(sorted(tup1))
# print(sorted(tup1, reverse=True))
# print(tup1[2])
# print(tup1[1:-1])
# print(tup1.count(2))
# print(tup1.index(3))
# tup1[2] = 10 # Tuples are immutable
t1 = (10, 20, 30)
t2 = (40, 50, 60)
t3 = t1 + t2
# print(t3)
# t4 = t3 * 2
# print(t4) 
# print(20 in t4)

# for v in tup1:
#     print(v)

# print(t3[2:-1])
# print(t3[1:-2])

# import sys 
# list = [1, 2, 3, 4, 5]
# tuple = (1, 2, 3, 4, 5)
# print("Size of list:", sys.getsizeof(list))
# print("Size of tuple:", sys.getsizeof(tuple))

myDict = {
    "name": "Hasnain",
    "age": 25,
    "city": "Karachi"
}

if "name" in myDict:
    print("Found 'name' in myDict")
if myDict.get("age") == 25:
    print("Age is 25")
if myDict.get("country") is None:
    print("Country key not found in myDict")
if "age" in myDict:
    del myDict["age"]

d = {
    "x": 10,
    "y": 20,
    "z": 30
}
for keys, values in d.items():
    print(f"{keys} : {values}")
for key in d.keys():
    print(key)
for value in d.values():
    print(value)