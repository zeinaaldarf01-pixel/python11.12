#task 1
i=1
while i<=20:
    if i==13:
        break
    print(i)
    i+=1
    #task 2
    count=0
    while True:
        num=int(input("Enter a number: "))
        if num==0:
            break
        count+=1    
    print("Total numbers entered:", count)
#task 3
name="development"
for char in name:
    print(char)
#task 4
oddcounter=0
for i in range (1,50):
    if i%2==0:
        print("Current number is", i, "there are", oddcounter, "odd number before that number")
    else: 
        oddcounter+=1
#task 5
for i in range (5):
    for j in range (5):
        print("*", end="")
    print()
#task 6
for i in range (0,5):
    for j in range (0,i+1):
        print("*", end="")
    print()
    #so proud
#task 7
