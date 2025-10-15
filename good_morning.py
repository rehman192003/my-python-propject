import time
a="good morning sir"
b="good afternoon sir"
c="good evening sir"
hr=int(time.strftime('%I'))
ampm=time.strftime('%p')
if ampm=="AM":
    if hr>=5 and hr<12:
        print(a)
    else:
        print(c)
else:
    if hr>=12 and hr<5:
        print(b)
    else:
        print(c)
