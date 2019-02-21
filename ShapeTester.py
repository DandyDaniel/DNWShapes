import math
from Box import Box
from Sphere import Sphere
from Pyramid import Pyramid

class ShapeTester:
    print('Welcome to the Shape Tester')
    print('Please type \'Box\', \'Sphere\', or \'Pyramid\'')
    while True
    i= input('>')
    if i == 'Box':
        print('Alright, let us start with a box.')
        width= int(input("Please enter a width:"))
        length= int(input("Please input a length: "))
        height= int(input("Please input a height: "))
        b1=Box(width,length,height)
        print('Volume: %s' % b1.getVolume())
        print('Surface Area: %s' % b1.getSA())
    elif i == 'Sphere':
        print('Alright, let us start with a sphere.')
        radius = int(input("Please enter a radius: "))
        s1=Sphere(radius)
        print('Volume: %s' % s1.getVolume())
        print('Surface Area: %s' % s1.getSA())
    elif i == 'Pyramid':
        print('Alright, let us start with a pyramid.')
        width= int(input("Please enter a width:"))
        length= int(input("Please input a length: "))
        height= int(input("Please input a height: "))
        p1=Pyramid(length,width,height)
        print('Volume: %s' % p1.getVolume())
        print('Surface Area: %s' % p1.getSA())
    else:
        print('mmmmmmm, try again.')
