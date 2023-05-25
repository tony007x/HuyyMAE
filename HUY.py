x = int(input("Price: "))
buy = int(input("How many: "))
box=[]
for i in range(buy):
    num = int(input())
    box.append(num)
for i in range(len(box)):
    print(box[i],"",x,"*",x)