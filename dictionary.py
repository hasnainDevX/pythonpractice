dict = {} # empty dictionary
print(dict)

dict = {
    "name": "Hasnain",
    "rollno" : "304",
    "sec": "abc"
}
print(dict)
if "name" in dict:
    del dict["name"]
print(dict)

for i in dict:
    print(f"{i} : {dict[i]}")

colorDict = {
    "red": "#FF000",
    "blue": "#fffff",
    "black": "#00000"
}

for keys in sorted(colorDict):
    print(keys)
    print(colorDict[keys])

mydict = {
    "numbers": [1,2,3,4,5],
    "names": ["one", "two", "three", "four", "five"]
}
print(mydict)
mydict.clear()
print(mydict)

mydict["numbers".capitalize]
print(mydict)

