#PythonAllTasks q70 random


import random
x=random.randint(1,100)
print(x)
y=int(input("Enter a number between 1 and 10"))
if y>0 and y<10:
    print("The average of",x, "and", y, "is",(x+y)/2)
else:
    print("That number was not between 1 and 10")

