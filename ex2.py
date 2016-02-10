print('Society in the beginning of XXI century\n')
x = int(raw_input('Input your age: '))
if x > 0 and x < 7:
    print('You should go to kindergarden')
elif x >= 7 and x < 18:
    print('You should go to school')
elif x >= 19 and x < 25:
    print('You should go to college')
elif x >= 25 and x < 60:
    print('You should go to work')
elif x >= 60 and x < 120:
    print('You\'ve granted a choice')
else:
    print('Error! It\'s only for humans!\n' * 5)