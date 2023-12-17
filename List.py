# countries =["pakistan" ,"india", "Europe"]
# countries[0]= "UK"
# print(countries)
# print(len(countries))
# print(type(countries))

# coutries =list(("Nigeria" , 34,342,243,False))
# print(coutries)


# list Method
list1 = [4,5,3,2,1]
list2= ["banana","apple","mangoes","orange","pomgrand"]
# list2.append("cheery")
# list1.extend(list2)
# list2.insert(1,"cheery")
# list2.remove("banana")
# # list2.clear()
# print(list2)
# print(list1)
# print(list2.index("mangoes"))
# print(len(list2))

# print(list2.count("apple"))

# accending order
list1.sort()
print(list1)

# decending order
list2.reverse()
print(list2)
list2.sort()
print(list2)



list3 =list2.copy()
list3.pop(2)
print(list3)

list3.remove("banana")
print(list3)

del list2[0]
print(list2)