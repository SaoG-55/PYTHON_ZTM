#EXCERCISE
# print * for 1 and " " for 0 from the given matrix
# pic=[
#     [0,0,0,1,0,0,0],
#     [0,0,1,1,1,0,0],
#     [0,1,1,1,1,1,0],
#     [1,1,1,1,1,1,1],
#     [0,0,0,1,0,0,0],
#     [0,0,0,1,0,0,0]
#     ]
pic=list()
for i in range(6):
    l1 = list()
    for j in range(7):
        x=int(input("enter 0 or 1"))
        l1.append(x)
    pic.append(l1)
print(pic)

for i in pic:
     for j in i:
         if(j==0):
             print(" ",end="")
         else:
             print("*",end="")
     print("")

