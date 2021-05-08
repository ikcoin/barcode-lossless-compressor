#!/usr/bin/env python3

import numpy as np
import imageio
import sys


img = imageio.imread(sys.argv[1])


############################## RL ENCODING #####################################
def rle_encode(data):
    encoding = []
    prev_char = ''
    count = 1

    for el in data:
        if el != prev_char:

            if prev_char != '':
                encoding.append(count)
                encoding.append(prev_char)
                
            count = 1
            prev_char = el
        else:
            count += 1
    else:
        encoding.append(count)
        encoding.append(prev_char)
    return encoding

############################## RL ENCODING #####################################


############################## FIND ENDS #####################################

shape_x = img.shape[1]
shape_y = img.shape[0]

primeraLinea = 0
segonaLinea = 0
ultimaRepetida = 0
margeInferior = 0

for fila in range(img.shape[0]):
    for columna in range(img.shape[1]):
        if img[fila][columna] != 255:
            if primeraLinea == 0:
                primeraLinea = fila
                segonaLinea = fila+1


segonaLinea = img[segonaLinea]

for x in range(primeraLinea+1, img.shape[0]):
    
    if False in (img[x] == segonaLinea):
        if ultimaRepetida == 0:
            ultimaRepetida = x


for i in range(img.shape[0]):
    if img[i][12] != 255:
        margeInferior = i


            
#Left Margin
leftMargin = 0
           
a = len(img[ultimaRepetida+1])
a = a/2

for i in range(int(a)):
    if img[ultimaRepetida+1][i] != 255:
        leftMargin = i

leftMargin += 1
            
            
#Right Margin
rightMargin = 0
anterior = 0

#for i in reversed(range(len(img[ultimaRepetida]))):
for i in reversed(range(img.shape[1])):
    if img[ultimaRepetida-1][i] != img[ultimaRepetida][i]:
        if rightMargin ==0:
            rightMargin = anterior
    anterior = i
            
            
            
############################## FIND ENDS #####################################




############################## RL ENCODING #####################################

wordBefore = np.array([[img[j][x] for x in range(leftMargin, rightMargin-1)] for j in range(ultimaRepetida+1, shape_y-7)])

wordBefore.resize(len(wordBefore) * len(wordBefore[1]))
total = (rle_encode(wordBefore))

############################## RL ENCODING #####################################




############################## WRITE #####################################

test1 = np.asarray(img[13]) #common row
test1 = test1.tolist()


#remove first and last 12 255
test = test1[12:-12]


#write
with open(sys.argv[2], "wb+") as f:
    
    #header
    f.write(shape_y.to_bytes(2, byteorder="big", signed=False))
    f.write(shape_x.to_bytes(2, byteorder="big", signed=False))
    
    f.write(leftMargin.to_bytes(2, byteorder="big", signed=False))
    f.write(rightMargin.to_bytes(2, byteorder="big", signed=False))
    f.write(margeInferior.to_bytes(2, byteorder="big", signed=False))

    f.write(len(total).to_bytes(2, byteorder="big", signed=False))

    
    for i in range(len(test)):
        f.write(test[i].to_bytes(2, byteorder="big", signed=False))
    
    for i in range(12, leftMargin):
        f.write(int(img[margeInferior][i]).to_bytes(2, byteorder="big", signed=False))
    
    for i in range(rightMargin, shape_x):
        f.write(int(img[margeInferior][i]).to_bytes(2, byteorder="big", signed=False))




    #word
    for j in range(len(total)):
    
        f.write(int(total[j]).to_bytes(2, byteorder="big", signed=False))

############################## WRITE #####################################




