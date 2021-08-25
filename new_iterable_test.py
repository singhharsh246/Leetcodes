list1 = (1, 2, 3, 4, 5, 6)
list2 = (7, 8, 9, 10, 11, 12)


print(list1)
print(list2)

dang = [(list1, list2)]

for i, j in dang:
    print(i, j, sep="\n")

for i in list1:
    print(i, sep="\n")

for i in list2:
    print(i, sep="\n")