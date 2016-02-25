from datetime import datetime, date
import time

# 1


def intdate(nd):
    print datetime.date(datetime.strptime(str(nd), '%Y%m%d'))


def inttodate():
    nd = raw_input('Input a number in YYYYMMDD format: \n')
    try:
        int(nd)
        ndcheck = 1
    except ValueError:
        ndcheck = 0
    if ndcheck == 0:
        print 'You must type only numbers! \n'
        inttodate()
    elif ndcheck == 1 and len(str(nd)) == 8:
        intdate(nd)
    elif ndcheck == 1 and len(str(nd)) != 8:
        print 'You must type exactly 8 numbers'
        inttodate()


# 2

def threenumbdate():
    day = int(raw_input('Input a day: '))
    month = int(raw_input('Input a month: '))
    year = int(raw_input('Input a year: '))
    dt = date(year, month, day)
    print dt


# 3
def stringtodate():
    nd = raw_input('Input a date in YYYYMMDD format: ')
    intdate(nd)

# 4


# 5


# 6

def todaywhichday():
    d = date.today()
    print d.strftime('%j')


# 7


def dateformat():
    dt = str(raw_input('Input a date in dd.mm.yyyy format: '))
    dd = datetime.date(datetime.strptime(dt, '%d.%m.%Y'))
    dm = time.strftime('%B %d %y', dd.timetuple())
    print dm
