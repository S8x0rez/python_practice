import math

def primeNumber():
    num = int(input())
    judge = False
    for i in range(2,int(math.sqrt(num)) + 1):
        if num % i == 0:
            judge = True
            break

    if judge:
        print("true")
    else:
        print("false")

import numpy as np

def generateImage():
    binImage = np.random.randint(0, 255, (32,32))
    return binImage

def countColor(img):
    array = np.zeros(26)
    for k in range(0, img.shape[0]):
        for j in range(0, img.shape[1]):
            array[int(img[k][j]/10)] += 1

    return array

import matplotlib.pyplot as plt

def printBar(array):
    plt.bar(range(0, 26), array, color='blue')
    plt.show()

def printImage(img):
    fig, ax = plt.subplots()
    im = ax.imshow(img, cmap='gray')
    plt.colorbar(im)
    plt.show()

def printWave():
    pi = math.pi

    x = np.linspace(0, 2*pi, 100)
    y = np.sin(x)
    print(y)

    plt.plot(x, y)
    plt.show()
