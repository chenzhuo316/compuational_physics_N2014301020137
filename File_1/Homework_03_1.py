a=['    ##    ',' #  ##    ',' ######## ','   ###    ']
b=['          ','    ##    ','    ##   #','##########','   ###    ']
c=['    ###   ','    ##    ',' ####### ','    ##  # ']
d=['          ','    ###   ','    ##    ','##########','#   ##    ']
import time 
import os 
n=1 
k=1
while True:
    time.sleep(0.5) 
    i = os.system('cls') 
    if n%4 == 1:
        print a[0]
        print a[0]
        print a[0]
        print a[1]
        print a[2]
        print a[2]
        print a[0]
        print a[0]
        print a[0]
        print a[3]
    if n%4 == 2:
        print b[0]
        print b[1]
        print b[1]
        print b[1]
        print b[3]
        print b[3]
        print b[2]
        print b[1]
        print b[4]
        print b[0]
    if n%4 == 3:
        print c[0]
        print c[1]
        print c[1]
        print c[1]
        print c[2]
        print c[2]
        print c[3]
        print c[1]
        print c[1]
        print c[1]
    if n%4 == 0:
        print d[0]
        print d[1]
        print d[2]
        print d[4]
        print d[3]
        print d[3]
        print d[2]
        print d[2]
        print d[2]
        print d[0]
    n=n+1
