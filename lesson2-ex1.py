def lesson2():
    program = raw_input("""Please select a program:

1) max word with space splitter
2) max word with semicolon splitter
3) min word with user specified symbol
4) count words in sentence

Type number of program: \n""")

    if program == '1':
        space_max()
    elif program == '2':
        semicolon_max()
    elif program == '3':
        min_specified()
    elif program == '4':
        sent_count()
    elif program == 'exit':
        pass
    else:
        print 'You didn\'t select any program. Try again or type exit '
        lesson2()

def space_max():
    text = str(raw_input('Input your text: \n'))
    x = text.split(' ')
    print max(x, key=len)

def semicolon_max():
    text = str(raw_input('Input your text: \n'))
    x = text.split(';')
    print max(x, key=len)

def min_specified():
    symbol = str(raw_input('Type your specified symbol: \n'))
    text = str(raw_input('Input your text: \n'))
    x = text.split(symbol)
    print min(x, key=len)

def sent_count():
    text = str(raw_input('Input your sentence: \n'))
    x = text.split(' ')
    print len(x)

lesson2()