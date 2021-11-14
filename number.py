import random
import string
from copy import deepcopy

c=3
a1 =[[1,1,1,1,0],
     [1,1,1,0,0],
     [1,1,0,1,0],
     [1,0,1,1,0],
     [1,1,1,1,0],
     [1,1,1,1,0],
     [1,1,1,1,0]]
a2 =[[0,0,0,0,0],
     [1,1,1,1,0],
     [1,1,1,1,0],
     [0,0,0,0,0],
     [0,1,1,1,1],
     [0,1,1,1,1],
     [0,0,0,0,0]]
a3 =[[0,0,0,0,0],
     [1,1,1,1,0],
     [1,1,1,1,0],
     [0,0,0,0,0],
     [1,1,1,1,0],
     [1,1,1,1,0],
     [0,0,0,0,0]]
a4 =[[0,1,1,1,0],
     [0,1,1,1,0],
     [0,1,1,1,0],
     [0,0,0,0,0],
     [1,1,1,1,0],
     [1,1,1,1,0],
     [1,1,1,1,0]]
a5 =[[0,0,0,0,0],
     [0,1,1,1,1],
     [0,1,1,1,1],
     [0,0,0,0,0],
     [1,1,1,1,0],
     [1,1,1,1,0],
     [0,0,0,0,0]]
a6 =[[0,0,0,0,0],
     [0,1,1,1,1],
     [0,1,1,1,1],
     [0,0,0,0,0],
     [0,1,1,1,0],
     [0,1,1,1,0],
     [0,0,0,0,0]]
a7 =[[0,0,0,0,0],
     [1,1,1,1,0],
     [1,1,1,1,0],
     [1,1,1,1,0],
     [1,1,1,1,0],
     [1,1,1,1,0],
     [1,1,1,1,0]]
a8 =[[0,0,0,0,0],
     [0,1,1,1,0],
     [0,1,1,1,0],
     [0,0,0,0,0],
     [0,1,1,1,0],
     [0,1,1,1,0],
     [0,0,0,0,0]]
a9 =[[0,0,0,0,0],
     [0,1,1,1,0],
     [0,1,1,1,0],
     [0,0,0,0,0],
     [1,1,1,1,0],
     [1,1,1,1,0],
     [0,0,0,0,0]]
a0 =[[0,0,0,0,0],
     [0,1,1,1,0],
     [0,1,1,1,0],
     [0,1,1,1,0],
     [0,1,1,1,0],
     [0,1,1,1,0],
     [0,0,0,0,0]]

arr = [a0,a1,a2,a3,a4,a5,a6,a7,a8,a9]

def letter(num):
    letter_c = []
    for i in range(c):
        letter = random.choice(string.ascii_lowercase)
        letter_c.append(letter)
    letter_v = ''.join(letter_c)
    return letter_v



def draw_digit(a):
    mn = []
    array = []
    for i in range(len(a)):
        for s in range(c):
            array.append(deepcopy(a[i]))
            for j in range(len(a[i])):
                if (a[i][j]!=0):
                    array[i][j] = ' '*c
                else:
                    array[i][j] = letter(c)
            m = ''.join(map(str,array[i]))
            mn.append(m)
    mk = '\n'.join(map(str,mn))
    return mk


def draw_num(b,arr):
    k=[]
    number =[[],[],[],[],[],[],[]]

    while b/10>0:
        k.append(b%10)
        b=b//10
    k.reverse()

    for i in range(7):
        for g in range(len(k)):
            for j in range(5):
                number[i].append(arr[k[g]][i][j])
            number[i].append(1)
    return draw_digit(number)

n=2001
print(draw_num(n,arr))

 
with open('listfile.txt', 'w') as filehandle:  
        filehandle.write(draw_num(n,arr))
