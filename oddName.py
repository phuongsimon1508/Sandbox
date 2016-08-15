""""
phuong tran
"""

name = input("Enter your name")
while name =="":
    name = input("Enter your name")

for i in range(1, len(name), 2):
    print(name[1], end='')