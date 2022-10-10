import re


def newer_stop(i):
    try: 
        print(i)
    except KeyboardInterrupt:
        return 'Остановка с клавиатуры'


i = 1
while i > 0:
    newer_stop(i)
    i += 1 