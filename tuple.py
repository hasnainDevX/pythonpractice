tup1 = () # empty tuple
tup2 = ("physics", "Chemistry", "Maths")
tup3 = (1,2,3,4)
print(tup1,"\n \b" ,tup2, "\n \b",tup3)

print(type(tup1)) # print data type

t4 = tuple("12345")
print(t4)


t5 = [1,5,7,8,9]
print(len(t5))
print(max(t5))
print(min(t5))

def avg(tup):
    sum = 0
    for i in tup:
        sum += i
    avg = sum / len(tup)
    print(avg)
avg(t5)

t6 = t5 * 4
print(t6)

print(2 in t5)
print(5 in t5)

for i in t5:
    print(i)

# list consumes more memory
# tuple consumes less memory
import sys
l = [3,4,5,9]
t = (2,4,6,7)
print(sys.getsizeof(l)) 
print(sys.getsizeof(t))
