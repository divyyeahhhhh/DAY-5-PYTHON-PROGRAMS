str=input("ENTER THE STRING,INPUT,S: ")
max_val=0

l1=str.split()
word=""

for i in l1:
    count = 0
    word=i

    for j in word:
        count+=1

    if max_val<count:
        max_val=count

print(count)
