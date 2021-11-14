import random
import string
import time
from copy import deepcopy

a1 =[[1,1,1,1,0],[1,1,1,0,0],[1,1,0,1,0],[1,0,1,1,0],[1,1,1,1,0],[1,1,1,1,0],[1,1,1,1,0]]
a2 =[[0,0,0,0,0],[1,1,1,1,0],[1,1,1,1,0],[0,0,0,0,0],[0,1,1,1,1],[0,1,1,1,1],[0,0,0,0,0]]
a3 =[[0,0,0,0,0],[1,1,1,1,0],[1,1,1,1,0],[0,0,0,0,0],[1,1,1,1,0],[1,1,1,1,0],[0,0,0,0,0]]
a4 =[[0,1,1,1,0],[0,1,1,1,0],[0,1,1,1,0],[0,0,0,0,0],[1,1,1,1,0],[1,1,1,1,0],[1,1,1,1,0]]
a5 =[[0,0,0,0,0],[0,1,1,1,1],[0,1,1,1,1],[0,0,0,0,0],[1,1,1,1,0],[1,1,1,1,0],[0,0,0,0,0]]
a6 =[[0,0,0,0,0],[0,1,1,1,1],[0,1,1,1,1],[0,0,0,0,0],[0,1,1,1,0],[0,1,1,1,0],[0,0,0,0,0]]
a7 =[[0,0,0,0,0],[1,1,1,1,0],[1,1,1,1,0],[1,1,1,1,0],[1,1,1,1,0],[1,1,1,1,0],[1,1,1,1,0]]
a8 =[[0,0,0,0,0],[0,1,1,1,0],[0,1,1,1,0],[0,0,0,0,0],[0,1,1,1,0],[0,1,1,1,0],[0,0,0,0,0]]
a9 =[[0,0,0,0,0],[0,1,1,1,0],[0,1,1,1,0],[0,0,0,0,0],[1,1,1,1,0],[1,1,1,1,0],[0,0,0,0,0]]
a0 =[[0,0,0,0,0],[0,1,1,1,0],[0,1,1,1,0],[0,1,1,1,0],[0,1,1,1,0],[0,1,1,1,0],[0,0,0,0,0]]

arr = [a0,a1,a2,a3,a4,a5,a6,a7,a8,a9]

с= int(input('Выбери циферку, пупсик '))

def letter(num):
    letter_c = []
    for i in range(с):
        letter = random.choice(string.ascii_lowercase)
        letter_c.append(letter)
    letter_v = ''.join(letter_c)
    return letter_v

def draw_digit(a):
    mn = []
    array = []
    for i in range(len(a)):
        for s in range(с):
            array.append(deepcopy(a[i]))
            for j in range(len(a[i])):
                if (a[i][j]!=0):
                    array[i][j] = ' '*с
                else:
                    array[i][j] = letter(с)
            m = ''.join(map(str,array[i]))
            mn.append(m)
    mk = '\n'.join(map(str,mn))
    return mk

def draw_num(b,arr):
    k=[]
    number =[[],[],[],[],[],[],[]]
    bb = int(b)
    for i in range(len(b)):
        k.append(bb%10)
        bb=bb//10
    k.reverse()

    for i in range(7):
        for g in range(len(k)):
            for j in range(5):
                number[i].append(arr[k[g]][i][j])
            number[i].append(1)
    return draw_digit(number)

def sys_time_output(): 
    t = time.time()
    while True:
        current_time = time.strftime('%H%M')
        num_current_time = str(current_time)
        if time.time()-t >= 1.0:
            t=time.time()
            print(draw_num(num_current_time,arr))

sys_time_output()
    