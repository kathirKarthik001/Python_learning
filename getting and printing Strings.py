a = []
print("enter a para :")
while True:
    b = input()
    if(b):
        a.append(b)
    else:
        break
c = "\t".join(a)
print(a)
print(c)
