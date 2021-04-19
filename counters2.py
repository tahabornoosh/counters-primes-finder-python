import math
n1 = int(input('number: '))
n2 = math.sqrt(n1)
n3 = 1
n4 = []
while n3 != round(n2)+1:
    if(n1 % n3 == 0):
        n4.append(n3)
        if(n3 != int(n1/n3)):
            n4.append(int(n1/n3))
    n3 +=1
print(sorted(n4))
