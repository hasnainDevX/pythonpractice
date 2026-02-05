from mymodule import greet, sum_numbers

print(greet("Alice"))
print(sum_numbers(5, 3))
# Output: Hello, Alice!
# Output: 8

import math as m
print(m.sqrt(16))
# Output: 4.0
print(m.pi)
# Output: 3.141592653589793
print(m.factorial(5))
# Output: 120
print(m.ceil(4.3))
# Output: 5
print(m.floor(4.7))
# Output: 4 
print(m.pow(2, 3))
# Output: 8.0
print(m.log(100, 10))
# Output: 2.0
print(m.gcd(48, 18))
# Output: 6
print(m.sin(m.pi/2))
import random
print(random.choice(['apple', 'banana', 'cherry']))
# Output: Randomly chosen fruit from the list
print(random.randint(1, 10))
# Output: Random integer between 1 and 10
print(random.random())
# Output: Random float between 0.0 and 1.0
print(random.uniform(2,4))