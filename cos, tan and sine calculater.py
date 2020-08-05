import time
import math
print('This program tells calculates the sine, cosine and tangent of the value you have inputed')
def cos():
    print('Type the integer!')
    z = int(input())
    time.sleep(1)
    cis = math.cos(z)
    time.sleep(1)
    print(cis)
    time.sleep(1)
    print('Do you want to start again')
    time.sleep
    print('Type "yes" , or "no"')
    abc = input()
    if abc == 'yes':
        begin()
    elif abc == 'no':
        print('Thank you for using! ')
    else:
        print('That was an invalid statment. The program will restart anyway.')
        begin()

def sin():
    time.sleep(1)
    print('Type the integer!')
    b = int(input())
    time.sleep(1)
    sine = math.sin(b)
    time.sleep(1)
    print(sine)
    time.sleep(1)
    print('Do you want to start again')
    time.sleep(1)
    print('Type "yes" , or "no"')
    c = input()
    if c == 'yes':
        print('Ok')
        begin()
    elif c == 'no':
        print('Thank you for using! ')
    else:
        print('That was an invalid statment. The program will restart anyway.')    
        begin()

def tan():
    print('Type the integer!')
    h = int(input())
    time.sleep(1)
    tani = math.tan(h)
    time.sleep(1)
    print(tani)
    time.sleep(1)
    print('Do you want to start again')
    print('Type "yes" , or "no"')
    d = input()
    if d == 'yes':
        begin()
    elif d == 'no':
        print('Thank you for using! ')
    else:
        print('That was an invalid statment. The program will restart anyway.')    
        begin()    




def main():
    print('What type of function do you want? ')
    time.sleep(0.5)
    print('sine ------- sin')
    time.sleep(1)
    print('cosine ------ cos')
    time.sleep(1)
    print('tangent -------- tan')
    time.sleep(0.5)
    y = input()
    
    if y == 'cos':
        print('Ok')
        cos()
    elif y == 'sin':
        print('Ok')
        sin()
    elif y == ('tan'):    
        tan()
    else:
        print('That was an invalid statment. Try again!!!')
        main()


def begin():
    print('Do you want to start?')
    time.sleep(1)
    print('Type "yes" or "no" ')
    time.sleep(1)
    x = input()
    if x == 'yes':
        print('Ok')
        main()
    elif x == 'no':
        print('Get out of here!!!')
    else:
        print('That was an invalid statment. Please try again')
        time.sleep(1)
        begin()
        
begin()        