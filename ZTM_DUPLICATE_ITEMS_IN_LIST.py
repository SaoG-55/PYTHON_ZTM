# remove duplicate items from the list
#suppose the user inputs duplicate numbers in the list the remove one of the duplicate numbers
list_dup=[]
n=int(input("Enter length"))
for i in range(n):
    x=int(input("enter no.s"))
    list_dup.append(x)
print(list_dup)
for i in list_dup:
    count_dup=list_dup.count(i)
    if(count_dup==2):
        list_dup.remove(i)
if(len(list_dup)!=n):
    print(f"After removing duplicate items the desired list is {list_dup}")
else:
    print("There were no duplicate elements in the list",list_dup)

