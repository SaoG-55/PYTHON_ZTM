#PRINT THE HIHEST EVEN NO. IN THE LIST USINF FUNCTION
def highest_even(li):
    max=0
    for i in li:
        if(i%2==0):
            if(max<i):
                max=i
    return max
num_list=list()
length=int(input("enter range of the list:"))
for i in range(length):
    x=int(input("Enter no."))
    num_list.append(x)
print(f"the list:{num_list}")
max_num=highest_even(num_list)
print(f"hihest even:{max_num}")

