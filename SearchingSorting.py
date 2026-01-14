def linearSearch(array, x,):
    for i in range(0, len(array)):
        if array[i] == x:
            return i
    return "No value found"

array = [2,5,66,88, 44, 77, 45, 23, 45]
print(linearSearch(array, 55))

def Search(array, targetIdx):
    x = array[targetIdx]
    return x

print(Search(array, 5))

vowels = ["a", "u", "o", "i", "e"]
vowels.sort()
print(vowels)

print(sorted(vowels, reverse=True))