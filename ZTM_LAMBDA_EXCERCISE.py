li = []
r = int(input("Enter the range"))
for i in range(r):
    x = int(input("no."))
    li.append(x)
print(f"list:{li}")

# # using lambda to sq the element of the list
print(f"Sq of the items: {list(map(lambda item: item ** 2, li))} ")
print(li)

l1 = []
for i in range(r):
    t = list()
    print("--Tuple--")
    for j in range(2):
        x = int(input("no."))
        t.append(x)
    t = tuple(t)
    l1.append(t)
print(f"List of tuples: {l1}")
# [(0,2),(4,3),(9,9),(10,-1)]
l1.sort()
# sorts wrt to the the 1st no. in tuple of list
print(f"sorted list wrt to 1st element{l1}")

# #sorting wrt to the 2nd no.
l1.sort(key=lambda x: x[1])
# extract each tuple from list and sorts acc to 2nd element
print(f"sorted list wrt to 2nd element{l1}")
