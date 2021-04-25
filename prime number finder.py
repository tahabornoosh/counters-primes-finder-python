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

range = 1000
loop = 1
res = []
tm = time.time()
while range != loop:
    if(len(counterfinder(loop)) == 2):
        print('finded 1 '+str(loop))
        res.append(loop)
    loop = loop + 1
print(res)
print('time: ',time.time() - tm, 'Secondes')