list1 = ['a', 'b', 'c', 'd', 'e']
for i in list1:
    print(i)

list2 = ['a', 'b', 'c', 'd', 'e']
for i in range(len(list2)):
    print(i)

# HAS to be a list of ints, b/c str throws error
list3 = [1,2,3,4,5]
for i in range(list3[0], list3[-1]):
    print(i)
