'''
由i控制輸出類型
*   i=1  j=1
**  i=1. j=2
*** i=1. j=3
1  1   i=2 j=1
22 22  i=2 j=2
333333 i=2 j=3
A  A  A  I=3 j=1
BB BB BB I=3 j=2
CCCCCCCCC I=3 j=3
1  2  3  4  I=4 j=1
11 22 33 44 I=4 j=2
111222333444 I=4 j=3
1  1  1  1  1  I=5 j=1
12 12 12 12 12 I=5 j=2
123123123123123 I=5 j=3
'''

for i in range(1,5+1):
    for j in range(1,3+1):
        for k in range(i):
            if i==1 :
                print(j*'*',end='')
            if i==2 :
                print(j*str(j)+(3-j)*' ',end='')
            if i==3 :
                print(j*chr(64+j)+(3-j)*' ',end='')
            if i==4 :
                print(j*str(k+1)+(3-j)*' ',end='')
            if i==5 :
                print('123'[0:j]+(3-j)*' ',end='')
        print()
