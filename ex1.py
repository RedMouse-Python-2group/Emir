x = int(raw_input('Input a number in range 1-9: '))
if x >= 1 and x <= 3:
    s = str(raw_input('Please, give a string: '))
    n = int(raw_input('Please, give a multiplier: '))
    for n in s:
        print s
elif x >= 4 and x <= 6:
    m = int(raw_input('Please, give a power of number: '))
    print(x ** m)
elif x >= 7 and x <= 9:
    for k in range(x, x+10):
        k += 1
        print k
