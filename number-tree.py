import math
import time
def counterfinder(input):
    n1 = int(input)
    n2 = math.sqrt(n1)
    n3 = 1
    n4 = []
    while n3 != round(n2)+1:
        if(n1 % n3 == 0):
            n4.append(n3)
            if(n3 != int(n1/n3)):
                n4.append(int(n1/n3))
        n3 +=1
    return(sorted(n4))


def prime(range):
    loop = 1
    res = []
    tm = time.time()
    while range != loop:
        if(len(counterfinder(loop)) == 2):
            #print('finded 1 '+str(loop))
            res.append(loop)
        loop = loop + 1
    return res

nums = []
temp = 0
num = int(input('Number to find'))
num2 = prime(num)
loop = 0
while loop != len(num2):
    if(num % num2[loop] == 0):
        temp = num
        while temp % num2[loop] == 0:
            nums.append(num2[loop])
            temp = temp/num2[loop]
        temp = 0
    loop = loop + 1
print(nums)