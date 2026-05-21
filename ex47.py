import time
for c in range (1, 51):
    if c % 2 == 0:
        time.sleep(0.1)
        print("{} é par".format(c))