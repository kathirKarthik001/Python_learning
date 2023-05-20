# python program to check for 3 digit numbers
n = int(input("Enter the number:"))
a = len(str(n))
if n >= 100 and n<1000 :
    print("3 digit number")
elif n >-1000 and n<=-100:
    print(" 3 digit number")
else:
    print("Not a 3 digit number")